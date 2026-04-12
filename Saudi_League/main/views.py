from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def base_view(request: HttpRequest):
    return render(request, "main/base.html")

def home_view(request: HttpRequest) :
    return render(request, "main/home.html")

def football_male_view(request: HttpRequest) :
    return render(request, "main/football_male.html")

def football_female_view(request: HttpRequest) :
    return render(request, "main/football_female.html")

def stadiums_view(request: HttpRequest) :
    return render(request, "main/stadiums.html")

def worldcup2034_view(request: HttpRequest):
    return render(request, "main/worldcup2034.html")

def moments_view(request: HttpRequest):
    return render(request, "main/unforgettable_moments.html")

def contact_us_view(request: HttpRequest) :
    return render(request, "main/contact_us.html")

def mode_view(request: HttpRequest, mode) :
    response = redirect(request.GET.get("next", "/"))
    if mode == 'dark' :
        response.set_cookie('mode', 'dark', max_age=24*60*60, path='/', samesite='Lax')
    elif mode == 'light' :
        response.set_cookie('mode', 'light', max_age=24*60*60, path='/', samesite='Lax')

    return response