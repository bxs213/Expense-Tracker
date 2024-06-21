from django.shortcuts import render, HttpResponse


# Create your views here.


def home(request):
    return render(request, "home.html")


def contact_us(request):
    return render(request, "contact_us.html")


def bootstrap(request):
    return render(request, "bootstrap.html")
