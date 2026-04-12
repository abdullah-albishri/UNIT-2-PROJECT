from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
    path('', views.home_view, name="home"),
    path('football_male/', views.football_male_view, name="football_male"),
    path('football_female/', views.football_female_view, name="football_female"),
    path('stadiums/', views.stadiums_view, name="stadiums"),
    path('moments/', views.moments_view, name="moments"),
    path('worldcup2034/', views.worldcup2034_view, name="worldcup2034"),
    path('contact_us/', views.contact_us_view, name="contact_us"),
    path('mode/<mode>/',views.mode_view, name='mode_view'),

]