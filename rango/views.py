from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    hello_partner = "Rango says hey there partner! " + '<a href="/rango/about/">About</a>'
    return HttpResponse(hello_partner)

def about(request):
    return HttpResponse("Rango says here is the about page. " + "<a href='/rango/'>Index</a>")