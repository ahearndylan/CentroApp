from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

def donate(request):
    return render(request, 'donate.html')

def news(request):
    return render(request, 'news.html')

def calendar(request):
    return render(request, 'calendar.html')

def careers(request):
    return render(request, 'contact/careers.html')

def members(request):
    return render(request, 'contact/members.html')

def privacy(request):
    return render(request, 'contact/privacy.html')

def terms(request):
    return render(request, 'contact/terms.html')

def compliance(request):
    return render(request, 'forms/compliance.html')

def referral(request):
    return render(request, 'forms/referral.html')

def children(request):
    return render(request, 'programs/children.html')

def community(request):
    return render(request, 'programs/community.html')

def family(request):
    return render(request, 'programs/family.html')

def financial(request):
    return render(request, 'programs/financial.html')

def food(request):
    return render(request, 'programs/food.html')

def foster(request):
    return render(request, 'programs/foster.html')

def homeowner(request):
    return render(request, 'programs/homeowner.html')

def ilac(request):
    return render(request, 'programs/ilac.html')

def nacdc(request):
    return render(request, 'programs/nacdc.html')

def rebuild(request):
    return render(request, 'programs/rebuild.html')

def contact(request):
    return render(request, 'contact.html')

def forms(request):
    return render(request, 'forms.html')



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            subject = f"Contact Form Submission"
            full_message = (
                f"Message from {first_name} {last_name}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n\n"
                f"{message}"
            )
            
            try:
                send_mail(
                    subject,
                    full_message,
                    settings.DEFAULT_FROM_EMAIL,
                    ['contactcentroinc@gmail.com'], 
                )
                return redirect('contact_success') 
            except Exception as e:
                print(f"Error sending email: {e}")
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'contact_success.html')