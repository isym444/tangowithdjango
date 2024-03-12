from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category, Page

# Create your views here.
def index(request):
    #context_dict={'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!','normalmessage':'This is just a normal message'}
    #html = "Rango says hey there partner!" + '<a href="/rango/about/">About</a>'
    #return HttpResponse(html)
    #return render(request, 'rango/index.html', context=context_dict)

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by the number of likes in descending order.
    # Retrieve the top 5 only -- or all if less than 5.
    # Place the list in our context_dict dictionary (with our boldmessage!) # that will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    top_pages_list = Page.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = top_pages_list
    # Render the response and send it back!
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'test':'here is the about page.'}
    #return HttpResponse("Rango says here is the about page.<a href='/rango/'>Index</a>")
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context=context_dict)

def show_page(request, page_name_slug):
    context_dict = {}
    try:
        page = Page.objects.get(slug=page_name_slug)
        context_dict['page'] = page
    except Page.DoesNotExist:
        context_dict['page'] = None
    return render(request, 'rango/page.html', context=context_dict)