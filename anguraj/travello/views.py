from django.shortcuts import render
from .models import Destination, Contact, Team


def index(request):
    dests = Destination.objects.all()
    profile = Contact.objects.all()
    return render(request, 'index.html', {'dests': dests, 'profile': profile})


def contact(request):
    profile = Contact.objects.all()
    return render(request, 'contact.html', {'profile': profile})


def about(request):
    team = Team.objects.all()
    profile = Contact.objects.all()
    return render(request, 'about.html', {'profile': profile, 'team': team})


def news(request):
    profile = Contact.objects.all()
    return render(request, 'news.html', {'profile': profile})


def destination(request):
    profile = Contact.objects.all()
    return render(request, 'destinations.html', {'profile': profile})


def home(request):
    dests = Destination.objects.all()
    profile = Contact.objects.all()
    return render(request, 'index.html', {'dests': dests, 'profile': profile})



