from django import forms
from tinymce.models import HTMLField
from .models import Contact, Enroll, level

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phonenumber', 'subject', 'questionfeedback')

class EnrollForm(forms.ModelForm):
    class Meta:
        model = Enroll
        exclude = []
        widgets = {
            'level': forms.CheckboxSelectMultiple(),
        }
