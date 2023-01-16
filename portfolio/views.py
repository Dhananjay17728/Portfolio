from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import Contact

# Create your views here.
def index(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('message')
        contact=Contact( name=name,email=email,phonenumber=phone,description=desc)
        contact.save()
        messages.success(request, 'Message sent successfully')
        return redirect("/contact")
    return render(request,"contact.html")
def project(request):
    return render(request,"project.html")
def resume(request):
    return render(request,"resume.html")
def ccc(request):
    return render(request,"ccc.html")
def ic(request):
    return render(request,"ic.html")
def mrs(request):
    return render(request,"mrs.html")
def weather(request):
    return render(request,"weather.html")




