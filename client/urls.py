from django.contrib import admin
from django.urls import path
from .views import ClientListView, ClientDetailView, ClientCreateView, ClientDeleteView, ClientUpdateView

app_name = "client"
urlpatterns = [
    path("client_list", ClientListView.as_view(), name='list'),
    path("client_detail/<int:pk>", ClientDetailView.as_view(), name='detail'),
    path("create", ClientCreateView.as_view(), name="create"),
    path("delete/<int:pk>", ClientDeleteView.as_view(), name="delete"),
    path("update/<int:pk>", ClientUpdateView.as_view(), name="update"),

]
