from django.forms import ModelForm
from client.models import Client


class ClientFrom(ModelForm):
    class Meta:
        model = Client
        fields = ["client_name", "zip_code", "pref", "city", "address", "visitplan"]

