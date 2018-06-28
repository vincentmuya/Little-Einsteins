from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .forms import ContactForm,EnrollForm
from django.http import JsonResponse
import datetime as dt

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
            return render(request, 'index.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form':form})

def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)

def enroll(request):
    if request.method == 'POST':
        eform = EnrollForm(request.POST)
        if eform.is_valid():
            enroll = eform.save(commit=False)
            enroll.save()
            return render(request, 'index.html')
    else:
        eform = EnrollForm()
    return render(request, 'enroll.html', {'eform':eform})
