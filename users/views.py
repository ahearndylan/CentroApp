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
from .forms import SubscribeForm
from .models import ContactMessage
from .forms import ComplianceForm
from .models import ComplianceMessage
from django.core.files.base import ContentFile
import os
from .models import Referral
from .forms import SubscribeForm
from .models import Subscriber
from .models import CalendarImage, CalendarEvent
from datetime import date
from .models import Donor
from .models import CentroStaff, BoardMember
from .models import NewsArticle
from .models import PartnerLogo
from .models import Review
from .models import FoodPantryLocation
from .models import CommunitySupportContact
from .models import FamilySupportHours
from .models import FamilySupportContact
from .models import ChildrenServicesContact
from .models import NACDCContact, NACDCBoardMember
from .models import HousingCounselorContact
from .models import RebuildingTestimonial
from .models import ILACImage
from .forms import SubscribeForm
from .models import SuggestionBoxMessage
from .forms import SuggestionBoxForm





#def home(request):
    #return render(request, 'home.html')

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

#def children(request):
    #return render(request, 'programs/children.html')

def community(request):
    return render(request, 'programs/community.html')

#def family(request):
    #return render(request, 'programs/family.html')

def financial(request):
    return render(request, 'programs/financial.html')

#def food(request):
    #return render(request, 'programs/food.html')

def foster(request):
    return render(request, 'programs/foster.html')

#def homeowner(request):
    #return render(request, 'programs/homeowner.html')

#def ilac(request):
    #return render(request, 'programs/ilac.html')

#def nacdc(request):
    #return render(request, 'programs/nacdc.html')

#def rebuild(request):
    #return render(request, 'programs/rebuild.html')

def contact(request):
    return render(request, 'contact.html')

def forms(request):
    return render(request, 'forms.html')

def suggestion_box_view(request):
    if request.method == 'POST':
        form = SuggestionBoxForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suggestions_success')
    else:
        form = SuggestionBoxForm()
    return render(request, 'forms/suggestions.html', {'form': form})


def suggestions_success(request):
    return render(request, 'forms/suggestions_success.html')




def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message'],
            )
            return redirect('contact_success') 
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'contact_success.html')


def compliance_view(request):
    if request.method == 'POST':
        form = ComplianceForm(request.POST)
        if form.is_valid():
            ComplianceMessage.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message'],
            )
            return redirect('compliance_success')  
    else:
        form = ComplianceForm()

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
            pdf_filename = f"{referral_data['first_name']}_{referral_data['last_name']}_referral.pdf"

            referral = Referral(
                first_name=referral_data['first_name'],
                last_name=referral_data['last_name'],
                email=referral_data['email'],
                date_of_birth=referral_data['date_of_birth'],
                program_or_services=referral_data['program_or_services'],
            )

            referral.pdf_file.save(pdf_filename, ContentFile(pdf_content))
            referral.save()

            return redirect('referral_success')
        else:
            print(form.errors)  
    else:
        form = ReferralForm()
    
    return render(request, "forms/referral.html", {"form": form})

def referral_success(request):
    return render(request, 'forms/referral_success.html')

def subscribe_view(request):
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            full_name = form.cleaned_data['full_name']
            
            if Subscriber.objects.filter(email=email).exists():
                return render(
                    request,
                    'base.html', 
                    {"subscribe_form": form, "subscribe_error": "This email is already subscribed."}
                )

            Subscriber.objects.create(
                full_name=full_name,
                email=email
            )
            return redirect('subscribe_success')  
        else:
            return render(request, 'base.html', {"subscribe_form": form, "subscribe_errors": form.errors})
    else:
        form = SubscribeForm()
    return render(request, 'base.html', {"subscribe_form": form})

    
def subscribe_success_view(request):
    return render(request, 'subscribe_success.html')

def calendar(request):
    today = date.today()
    current_month_image = CalendarImage.objects.filter(month=today.strftime("%B"), year=today.year).first()

    current_month_events = CalendarEvent.objects.filter(
        date__year=today.year,
        date__month=today.month
    )

    context = {
        'current_month_image': current_month_image,
        'current_month_events': current_month_events,
    }
    return render(request, 'calendar.html', context)


def donate(request):
    donor_images = Donor.objects.all()
    return render(request, 'donate.html', {'donor_images': donor_images})

def team(request):
    staff_members = CentroStaff.objects.all()
    board_members = BoardMember.objects.all()
    context = {
        'staff_members': staff_members,
        'board_members': board_members,
    }
    return render(request, 'team.html', context)


def news(request):
    dynamic_articles = NewsArticle.objects.all().order_by("-publish_date")
    return render(request, 'news.html', {'dynamic_articles': dynamic_articles})

def home(request):
    logos = PartnerLogo.objects.all()[:5]
    reviews = Review.objects.all().order_by('-created_at')  # optional limit: [:10]
    news_articles = NewsArticle.objects.filter(featured_on_homepage=True)[:4]
    subscribe_form = SubscribeForm()

    return render(request, 'home.html', {
        'partner_logos': logos,
        'reviews': reviews,
        'news_articles': news_articles,
        'subscribe_form': subscribe_form,
    })

def food(request):
    locations = FoodPantryLocation.objects.order_by('order')
    return render(request, 'programs/food.html', {
        'locations': locations,
    })

def community(request):
    contact = CommunitySupportContact.objects.first()
    return render(request, 'programs/community.html', {'contact': contact})

def family(request):
    hours = FamilySupportHours.objects.first()
    contact = FamilySupportContact.objects.first()
    return render(request, 'programs/family.html', {
        'support_hours': hours,
        'contact': contact
    })

def children(request):
    contact = ChildrenServicesContact.objects.first()
    return render(request, 'programs/children.html', {
        'contact': contact
    })

def nacdc(request):
    contact = NACDCContact.objects.first()
    board_members = NACDCBoardMember.objects.all()
    return render(request, 'programs/nacdc.html', {
        'contact': contact,
        'board_members': board_members,
    })

def homeowner(request):
    contact = HousingCounselorContact.objects.first()
    return render(request, 'programs/homeowner.html', {
        'contact': contact
    })

def rebuild(request):
    testimonials = RebuildingTestimonial.objects.order_by('-created_at')
    return render(request, 'programs/rebuild.html', {'testimonials': testimonials})

def ilac(request):
    ilac_images = ILACImage.objects.all()
    return render(request, 'programs/ilac.html', {'ilac_images': ilac_images})