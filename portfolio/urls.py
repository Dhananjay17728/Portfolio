from django.contrib import admin
from django.urls import path,include
from portfolio import views

urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("project",views.project,name="project"),
    path("resume",views.resume,name="resume"),
    path("ic",views.ic,name="ic"),
    path("ccc",views.ccc,name="ccc"),
    path("mrs",views.mrs,name="mrs"),
    path("weather",views.weather,name="weather"),
    path("shopcart",views.shopcart,name="shopcart")
]
