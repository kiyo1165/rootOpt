from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from client.models import Client
from .forms import ClientFrom
from django.urls import reverse_lazy, reverse
from .google import getGoogleapi



# Create your views here.

class ClientListView(ListView):
    model = Client
    template_name = "client/client_list.html"
    context_object_name = "client_list"


class ClientDetailView(DetailView):
    model = Client
    template_name = "client/client_detail.html"
    context_object_name = "client_detail"


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientFrom
    success_url = reverse_lazy("client:list")
    template_name = "client/client_form.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # 住所を結合
        address = self.object.city+self.object.address
        location = getGoogleapi(address)
        self.object.longitude = location['lat']
        self.object.latitude = location['lng']
        form.save()
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    fields = "__all__"
    template_name = "client/client_update.html"

    def get_success_url(self):
        return reverse('client:detail', kwargs={'pk': self.object.pk})


class ClientDeleteView(DeleteView):
    model = Client
    template_name = "client/client_delete.html"
    success_url = reverse_lazy("client:list")
