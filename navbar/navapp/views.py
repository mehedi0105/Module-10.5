from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about(request):
    return render(request, "navapp/about.html")


def contact(request):
    return render(request, "navapp/contact.html")