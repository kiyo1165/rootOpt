from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("dr/", include("Dr.urls")),
    path("admin/", admin.site.urls),
    path("client/", include("client.urls")),
]
