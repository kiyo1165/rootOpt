from django.shortcuts import render
from django.views.generic import ListView
from .models import Client
# Create your views here.

class ClientListView(ListView):
    model = Client
    template_name = "templates/client_list.html"
    context_object_name = "client_list"
