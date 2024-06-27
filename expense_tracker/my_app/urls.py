from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("bootstrap", views.bootstrap, name="bootstrap"),
    path("contact_us", views.contact_us, name="contact"),
]

