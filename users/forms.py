# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SubscribeForm(forms.Form):
    full_name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)

class ReferralForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    email = forms.EmailField(label="Email Address")  # Add this field
    date_of_birth = forms.DateField(label="Date of Birth", widget=forms.DateInput(format='%d-%m-%Y', attrs={'placeholder': 'DD/MM/YYYY'}))
    program_or_services = forms.CharField(label="Program or Services Requested", max_length=255)
    insurance_company = forms.CharField(label="Insurance Company", max_length=255)
    insurance_number = forms.CharField(label="Insurance Number or ID", max_length=100)
    preferred_language = forms.CharField(label="Preferred Language", max_length=100)
    street_address = forms.CharField(label="Street Address", max_length=255)
    address_line_2 = forms.CharField(label="Address Line 2", max_length=255, required=False)
    city = forms.CharField(label="City", max_length=100)
    state = forms.CharField(label="State/Region/Province", max_length=100)
    postal_code = forms.CharField(label="Postal/Zip Code", max_length=20)
    guardian_first_name = forms.CharField(label="Guardian First Name", max_length=100)
    guardian_last_name = forms.CharField(label="Guardian Last Name", max_length=100)
    guardian_phone = forms.CharField(label="Guardian Phone", max_length=20)
    guardian_email = forms.EmailField(label="Guardian Email Address")
    notes = forms.CharField(label="Notes or Message", widget=forms.Textarea, required=False)
    referred_by = forms.CharField(label="Referred By", max_length=100)
    date_of_referral = forms.DateField(label="Date of Referral", widget=forms.DateInput(format='%d-%m-%Y', attrs={'placeholder': 'DD/MM/YYYY'}))
    referral_phone = forms.CharField(label="Phone", max_length=20)
    referral_from = forms.CharField(label="From", max_length=100)


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

class ComplianceForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}), required=True)


class SubscribeForm(forms.Form):
    full_name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name*'}),
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email*'}),
        required=True
    )
