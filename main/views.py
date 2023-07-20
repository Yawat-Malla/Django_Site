from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def membership(request):
    return render(request, 'main/membership.html',{'title':'Get a Membership'})

def resources(request):
    return render(request, 'main/resources.html',{'title':'Resources'})

def team(request):
    return render(request, 'main/team.html',{'title':'Our Team'})

def contact(request):
    return render(request, 'main/contact.html',{'title':'Contact Us'})

def event(request):
    return render(request, 'main/event.html',{'title':'News and Events'})
