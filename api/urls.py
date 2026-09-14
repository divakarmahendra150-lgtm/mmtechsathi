from django.urls import path
from . import views



urlpatterns = [
    path("contact/", views.contact_api, name="contact_api"),
    path("health/", views.health_check, name="health_check"),

]
