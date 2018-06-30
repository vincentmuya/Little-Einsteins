from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .forms import ContactForm,EnrollForm
from django.http import JsonResponse
import datetime as dt
from django.core.mail import mail_admins

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
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            phonenumber = form.cleaned_data['phonenumber']
            subject = "You have a new Feedback from {}:{}".format(name, sender)
            questionfeedback = "Subject: {}\n\nquestionfeedback: {}\n\nphonenumber: {}".format(form.cleaned_data['subject'], form.cleaned_data['questionfeedback'], form.cleaned_data['phonenumber'])
            mail_admins(subject, questionfeedback)
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
            firstname = eform.cleaned_data['firstname']
            surname = eform.cleaned_data['surname']
            level = eform.cleaned_data['level']
            address = eform.cleaned_data['address']
            parentgurdianname = eform.cleaned_data['parentgurdianname']
            email = eform.cleaned_data['email']
            phonenumber = eform.cleaned_data['phonenumber']
            allergiesspecial = eform.cleaned_data['allergiesspecial']
            subject = "There is a new enrollment from {}:{}".format(parentgurdianname, email)
            enroll = "firstname: {}\n\nsurname: {}\n\nlevel: {}\n\naddress: {}\n\nparentgurdianname: {}\n\nemail: {}\n\nphonenumber: {}\n\nallergiesspecial: {}".format(eform.cleaned_data['firstname'], eform.cleaned_data['surname'], eform.cleaned_data['level'], eform.cleaned_data['address'], eform.cleaned_data['parentgurdianname'], eform.cleaned_data['email'], eform.cleaned_data['phonenumber'], eform.cleaned_data['allergiesspecial'])
            mail_admins(subject, enroll)
            enroll = eform.save(commit=False)
            enroll.save()
            return render(request, 'index.html')
    else:
        eform = EnrollForm()
    return render(request, 'enroll.html', {'eform':eform})
