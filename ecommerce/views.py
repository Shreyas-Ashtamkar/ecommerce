from django.http import HttpResponse
from django.shortcuts import  render

from .forms import ContactForm

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
    
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "content":"This is the Content.",
        "form" : contact_form
    }
    
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request,"contact/view.html", context)