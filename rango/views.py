from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    html = "Rango says hey there partner!" + '<a href="/rango/about/">About</a>'
    return HttpResponse(html)

def about(request):
    return HttpResponse("Rango says here is the about page.<a href='/rango/'>Index</a>")