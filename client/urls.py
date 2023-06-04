from django.contrib import admin
from django.urls import path
from .views import ClientListView, ClientDetailView, clientindex, ClientCreateView

app_name = "client"
urlpatterns = [
    # path("client_list", ClientListView.as_view(), name='list'),
    path("client_detail/<int:pk>", ClientDetailView.as_view(), name='detail'),
    path("client_list", clientindex, name="list"),
    path("create", ClientCreateView.as_view(), name="cliate")
]
