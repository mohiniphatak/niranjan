from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cfohubapp.models import Service


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False,label="Full Name", help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, label="Contact Number", help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1' )

class ServicesForm(forms.ModelForm):
    SERV = (
        ('2000', 'Created'),
        ('10', 'Changed'),
        ('2', 'Deleted'),
    )

    name = forms.CharField(max_length=30, required=False,label="Full Name", help_text='Optional.')
    contact = forms.CharField(max_length=30, required=True, label="Contact Number", help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    service = forms.ChoiceField(choices=SERV, label='Select Service')

    class Meta:
        model = Service
        fields = ('name', 'contact', 'email', 'service' )

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    # subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
