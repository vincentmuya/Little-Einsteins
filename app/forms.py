from django import forms
from tinymce.models import HTMLField
from .models import Contact, Enroll, Sponsor

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = []

class EnrollForm(forms.ModelForm):
    class Meta:
        model = Enroll
        exclude = []
        widgets = {
            'level': forms.CheckboxSelectMultiple(),
        }

class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        exclude = []
