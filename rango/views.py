from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict={'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!','normalmessage':'This is just a normal message'}
    #html = "Rango says hey there partner!" + '<a href="/rango/about/">About</a>'
    #return HttpResponse(html)
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'test':'here is the about page.'}
    #return HttpResponse("Rango says here is the about page.<a href='/rango/'>Index</a>")
    return render(request, 'rango/about.html', context=context_dict)