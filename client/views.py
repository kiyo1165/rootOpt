from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from client.models import Client
from django.shortcuts import render
from .forms import ClientFrom
from django.urls import reverse_lazy
import googlemaps
from .google import getGoogleapi



# Create your views here.

class ClientListView(ListView):
    model = Client
    template_name = "client/client_list.html"
    context_object_name = "client_list"


def clientindex(request):
    client_list = Client.objects.all()
    context = {
        "client_list": client_list,
    }
    return render(request, "client/client_list.html", context)


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



