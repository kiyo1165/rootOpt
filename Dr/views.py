
from django.views.generic import ListView, CreateView
from .models import VisitPlan, Dr
from .forms import VisitPlanForm
from client.google import getGoogleapi
from django.urls import reverse_lazy
# Create your views here.


class PlanListView(ListView):
    model = VisitPlan
    template_name = "dr/visitplan_list.html"
    content_object_name = "visitplan_lsit"

class PlanCreateView(CreateView):
    model = VisitPlan
    template_name = "dr/visitplan_form.html"
    form_class = VisitPlanForm
    success_url = reverse_lazy("dr:visitplan_list")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # 住所を結合
        address = self.object.city + self.object.address
        location = getGoogleapi(address)
        self.object.longitude = location['lat']
        self.object.latitude = location['lng']
        form.save()
        return super().form_valid(form)