# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    fname = forms.CharField(max_length=100, label="First Name")
    lname = forms.CharField(max_length=100, label="Last Name")
    phone = forms.CharField(max_length=15, label="Phone Number")
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'fname', 'lname', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['fname']
        user.last_name = self.cleaned_data['lname']
        user.email = self.cleaned_data['email']

        return user


class ContactForm(forms.Form):
    first_name = forms.CharField(
        max_length=50, required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=50, required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    phone = forms.CharField(
        max_length=15, required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'})
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}), 
        required=True
    )
