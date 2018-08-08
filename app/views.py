from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .forms import ContactForm,EnrollForm,SponsorForm
from django.http import JsonResponse
import datetime as dt
from django.core.mail import mail_admins
import googlemaps
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import requests

gmaps = googlemaps.Client(key='AIzaSyC14hiJhxMKNF4T4JCkDWyITjz8CoU2aco')
geo_result = gmaps.geocode('address')
print(geo_result)
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
            Name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            phonenumber = form.cleaned_data['phonenumber']
            subject = "You have a new Feedback from {}:{}".format(Name, sender)
            Question_or_Feedback = "Subject: {}\n\nQuestion_or_Feedback: {}\n\nphonenumber: {}".format(form.cleaned_data['subject'], form.cleaned_data['questionfeedback'], form.cleaned_data['phonenumber'])
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
            Firstname = eform.cleaned_data['Firstname']
            Surname = eform.cleaned_data['Surname']
            level = eform.cleaned_data['level']
            Address = eform.cleaned_data['Address']
            Parent_Gurdian_Name = eform.cleaned_data['Parent_Gurdian_Name']
            email = eform.cleaned_data['email']
            Phone_Number = eform.cleaned_data['Phone_Number']
            Allergies_or_Special_Needs = eform.cleaned_data['Allergies_or_Special_Needs']
            subject = "There is a new enrollment from {}:{}".format(Parent_Gurdian_Name, email)
            enroll = "Firstname: {}\n\nSurname: {}\n\nlevel: {}\n\nAddress: {}\n\nParent_Gurdian_Name: {}\n\nemail: {}\n\nphonenumber: {}\n\nallergiesspecial: {}".format(eform.cleaned_data['Firstname'], eform.cleaned_data['Surname'], eform.cleaned_data['level'], eform.cleaned_data['Address'], eform.cleaned_data['Parent_Gurdian_Name'], eform.cleaned_data['email'], eform.cleaned_data['Phone_Number'], eform.cleaned_data['Allergies_or_Special_Needs'])
            mail_admins(subject, enroll)
            enroll = eform.save(commit=False)
            enroll.save()
            return render(request, 'index.html')
    else:
        eform = EnrollForm()
    return render(request, 'enroll.html', {'eform':eform})
def sponsor(request):
    if request.method == 'POST':
        sform = SponsorForm(request.POST)
        if sform.is_valid():
            Firstname = sform.cleaned_data['Firstname']
            Surname = sform.cleaned_data['Surname']
            email = sform.cleaned_data['email']
            Phone_Number = sform.cleaned_data['Phone_Number']
            subject = "There is a new Sponsor {}:{}".format(Firstname, email)
            Sponsor = "Firstname: {}\n\nSurname: {}\n\nemail: {}\n\nPhone_Number: {}".format(sform.cleaned_data['Firstname'], sform.cleaned_data['Surname'],sform.cleaned_data['email'], sform.cleaned_data['Phone_Number'])
            mail_admins(subject, Sponsor)
            sponsor = sform.save(commit=False)
            sponsor.save()
            return render(request, 'index.html')
    else:
        sform = SponsorForm
    return render(request, "sponsor.html", {'sform':sform})

def location(request):
    test = "Code running"
    if 'address' in request.GET and request.GET['address']:
        address = request.GET.get('address')
        geo_result = gmaps.geocode('address')
        print(geo_result)
        latitude = geo_result[0]['geometry']['location'].get('lat')
        longitude = geo_result[0]['geometry']['location'].get('lng')
        location = Location()
        location.name = address
        location.latitude = latitude
        location.longitude = longitude
        location.time = dt.datetime.now()
        location.save()

        return render(request, "location.html", {"latitude":latitude,"longitude":longitude, "address":address})
    else:
        return render(request, 'location.html', {"test":test})
def annual(request):
    return render(request, 'annual.html')
def annual2018(request):
    return render(request, 'annual2018.html')
def learn(request):
    return render(request, 'learn.html')
def foundation(request):
    return render(request, 'foundation.html')
