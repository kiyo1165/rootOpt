from django.urls import path

from .views import PlanListView, PlanCreateView

app_name = "dr"
urlpatterns = [
    path("visitplan_list", PlanListView.as_view(), name="visitplan_list"),
    path("visitplan_create", PlanCreateView.as_view(), name="visitplan_create"),

]
