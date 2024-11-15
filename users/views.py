from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .forms import ComplianceForm
from django.core.mail import EmailMessage
from django.http import HttpResponse
from .forms import ReferralForm
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib import colors


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


def compliance_view(request):
    if request.method == 'POST':
        form = ComplianceForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            subject = f"Compliance Form Submission"
            full_message = f"Message from {first_name} {last_name} ({email}):\n\n{message}"
            
            try:
                send_mail(
                    subject,
                    full_message,
                    settings.DEFAULT_FROM_EMAIL,
                    ['contactcentroinc@gmail.com'], 
                )
                return redirect('compliance_success') 
            except Exception as e:
                print(f"Error sending email: {e}")
    else:
        form = ContactForm()
    
    return render(request, 'forms/compliance.html', {'form': form})

def compliance_success_view(request):
    return render(request, 'forms/compliance_success.html')




def generate_pdf(referral_data):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, 750, "Referral Form")  
    p.setFont("Helvetica", 10)

    p.setStrokeColor(colors.black)
    p.setLineWidth(1)
    p.line(50, 740, 550, 740)

    x_start = 50
    y_start = 720
    line_height = 18

    def draw_section_header(title, y_position):
        p.setFont("Helvetica-Bold", 12)
        p.drawString(x_start, y_position, title)
        p.line(x_start, y_position - 2, x_start + 500, y_position - 2)
        return y_position - line_height * 1.2

    def format_field_name(field_name):
        return field_name.replace("_", " ").title()  

    def draw_field(field, value, y_position):
        formatted_field = format_field_name(field)  
        p.setFont("Helvetica-Bold", 10)
        p.drawString(x_start, y_position, f"{formatted_field}:")
        p.setFont("Helvetica", 10)
        p.drawString(x_start + 150, y_position, str(value))
        return y_position - line_height

    sections = [
        ("Client Information", ["first_name", "last_name", "date_of_birth", "preferred_language"]),
        ("Program Details", ["program_or_services", "insurance_company", "insurance_number"]),
        ("Address", ["street_address", "address_line_2", "city", "state", "postal_code"]),
        ("Guardian Information", ["guardian_first_name", "guardian_last_name", "guardian_phone", "guardian_email"]),
        ("Referral Information", ["referred_by", "date_of_referral", "referral_phone", "referral_from"]),
    ]

    for section_title, fields in sections:
        y_start = draw_section_header(section_title, y_start)
        for field in fields:
            value = referral_data.get(field, "N/A")  
            y_start = draw_field(field, value, y_start)
        y_start -= line_height  

    p.setFont("Helvetica", 8)
    p.drawString(50, 20, "Generated by Centro Referral System")
    p.drawRightString(550, 20, "Page 1")

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    return pdf

def referral_view(request):
    if request.method == "POST":
        form = ReferralForm(request.POST)
        if form.is_valid():
            referral_data = form.cleaned_data
            
            pdf_content = generate_pdf(referral_data)
            
            email = EmailMessage(
                subject="General Referral Form",
                body="Please find the attached referral form.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.EMAIL_HOST_USER],  
            )
            email.attach("referral_form.pdf", pdf_content, "application/pdf")
            email.send()

            return redirect('referral_success')
        else:
            print(form.errors)  
    else:
        form = ReferralForm()
    
    return render(request, "forms/referral.html", {"form": form})

def referral_success(request):
    return render(request, 'forms/referral_success.html')