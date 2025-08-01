from django.db import models
from ckeditor.fields import RichTextField


class ComplianceMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

    class Meta:
        verbose_name = "Compliance Form"
        verbose_name_plural = "Compliance Forms"
        permissions = [
            ("view_compliance_message", "Can view compliance forms"),
        ]


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

    class Meta:
        verbose_name = "Contact Form"
        verbose_name_plural = "Contact Forms"
        permissions = [
            ("view_contact_message", "Can view contact forms"),
        ]

class Referral(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField(null=True, blank=True)
    program_or_services = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='referrals/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Referral"
        verbose_name_plural = "Referrals"
        permissions = []  

class Subscriber(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("can_view_subscribers", "Can view subscribers"),
        ]

    def __str__(self):
        return self.full_name
    
class CalendarImage(models.Model):
    month = models.CharField(max_length=20, unique=True)  
    year = models.IntegerField()  
    image = models.ImageField(upload_to='calendar_images/')  

    def __str__(self):
        return f"{self.month} {self.year}"


class CalendarEvent(models.Model):
    date = models.DateField(unique=True)  
    title = models.CharField(max_length=100)  
    description = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"{self.title} on {self.date}"
    
class Donor(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the donor")
    logo = models.ImageField(upload_to="donor_logos/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Donor Image"
        verbose_name_plural = "Donor Images"

class CentroStaff(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    headshot = models.ImageField(upload_to='staff_headshots/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BoardMember(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    quote = models.TextField()
    excerpt = models.TextField()
    body = RichTextField()
    author = models.CharField(max_length=100, default="vremos04")  
    publish_date = models.DateField(default=None, null=True, blank=True)
    read_time = models.CharField(max_length=50)  
    image = models.ImageField(upload_to="news_images/")
    external_link = models.URLField(blank=True, null=True)  

    featured_on_homepage = models.BooleanField(default=False)  # ✅ NEW FIELD

    def __str__(self):
        return self.title

class PartnerLogo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='partner_logos/')

    def __str__(self):
        return self.name
    
class Review(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Optional: number of stars (1-5)
    stars = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return f"{self.author} ({self.stars}⭐)"

class FoodPantryLocation(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    days_hours = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)  # to allow ordering in template

    def __str__(self):
        return self.name

class CommunitySupportContact(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class FamilySupportHours(models.Model):
    location = models.CharField(max_length=100, default="Worcester (Central)")
    days = models.CharField(max_length=100, default="Monday – Friday")
    time = models.CharField(max_length=100, default="9:00 AM – 5:00 PM")

    def __str__(self):
        return f"{self.location} Hours"

class FamilySupportContact(models.Model):
    location = models.CharField(max_length=100, default="Worcester")
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} ({self.location})"

class ChildrenServicesContact(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class NACDCContact(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    link_1_text = models.CharField(max_length=255, blank=True)
    link_1_url = models.URLField(blank=True)
    link_2_text = models.CharField(max_length=255, blank=True)
    link_2_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class NACDCBoardMember(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name} - {self.title}"
    

class HousingCounselorContact(models.Model):
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return "Housing Counselor Contact Info"


class RebuildingTestimonial(models.Model):
    name = models.CharField(max_length=100)
    quote = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ILACImage(models.Model):
    image = models.ImageField(upload_to='ilac_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption or f"ILAC Image {self.id}"
    
class SuggestionBoxMessage(models.Model):
    SUBMISSION_TYPES = [
        ('Complaint', 'Complaint'),
        ('Suggestion', 'Suggestion'),
        ('Survey', 'Survey'),
    ]

    submission_type = models.CharField(max_length=20, choices=SUBMISSION_TYPES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.submission_type} submitted on {self.created_at.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = "Suggestion Box Submission"
        verbose_name_plural = "Suggestion Box Submissions"
