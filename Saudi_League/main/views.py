from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def base_view(request: HttpRequest):
    return render(request, "main/base.html")

def home_view(request: HttpRequest) :
    return render(request, "main/home.html")
