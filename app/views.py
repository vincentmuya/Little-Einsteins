from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def program(request):
    return render(request, 'program.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact =form.save(commit=False)
            contact.save()
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})
