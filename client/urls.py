from django.contrib import admin
from django.urls import path
from .views import ClientListView, ClientDetailView

app_name = "client"
urlpatterns = [
    path("client_list", ClientListView.as_view(), name='list'),
    path("client_detail/<int:pk>", ClientDetailView.as_view(), name='detail')

]
