from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Client
# Create your views here.

class ClientListView(ListView):
    model = Client
    template_name = "client/client_list.html"
    context_object_name = "client_list"

class ClientDetailView(DetailView):
    model= Client
    template_name = "client/client_detail.html"
    context_object_name = "client_detail"