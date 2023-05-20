from django.contrib import admin
from django.urls import path
from .views import ClientListView

app_name = "client"
urlpatterns = [
    path("", ClientListView.as_view(), name="client_list")
]
