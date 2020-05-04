from django.http import HttpResponse
from django.shortcuts import  render

def home_page(request):
    context = {
        "title":"Home",
        "content":"This is the Content."
    }
    return render(request,"general_page.html", context)


def about_page(request):
    context = {
        "title": "About",
        "content":"This is the Content."
    }
    return render(request,"general_page.html", context)


def contact_page(request):
    context = {
        "title": "Contact",
        "content":"This is the Content."
    }
    return render(request,"contact/view.html", context)