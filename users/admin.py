from django.contrib import admin
from .models import ContactMessage
from django.contrib import admin
from .models import ComplianceMessage
from .models import Referral
from .models import Subscriber
from .models import CalendarImage, CalendarEvent
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
from .models import SuggestionBoxMessage





@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('created_at',)


@admin.register(ComplianceMessage)
class ComplianceMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('-created_at',)

@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('created_at',)

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'created_at')
    search_fields = ('full_name', 'email')
    list_filter = ('created_at',)

@admin.register(CalendarImage)
class CalendarImageAdmin(admin.ModelAdmin):
    list_display = ('month', 'year', 'image')
    search_fields = ('month', 'year')


@admin.register(CalendarEvent)
class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'description')
    search_fields = ('date', 'title')
    list_filter = ('date',)


@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

@admin.register(CentroStaff)
class CentroStaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'created_at')
    search_fields = ('name', 'title')


@admin.register(BoardMember)
class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'created_at')
    search_fields = ('name', 'title')


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish_date")
    search_fields = ("title", "author")
    ordering = ("-publish_date",)

@admin.register(PartnerLogo)
class PartnerLogoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'stars', 'created_at')
    search_fields = ('author', 'text')
    ordering = ('-created_at',)

@admin.register(FoodPantryLocation)
class FoodPantryLocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'days_hours', 'order']
    ordering = ['order']

@admin.register(CommunitySupportContact)
class CommunitySupportContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'phone', 'email')
    search_fields = ('name', 'role', 'email')

@admin.register(FamilySupportHours)
class FamilySupportHoursAdmin(admin.ModelAdmin):
    list_display = ('location', 'days', 'time')

@admin.register(FamilySupportContact)
class FamilySupportContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'position', 'phone', 'email')

@admin.register(ChildrenServicesContact)
class ChildrenServicesContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'phone', 'email')


@admin.register(NACDCContact)
class NACDCContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'phone', 'email')


@admin.register(NACDCBoardMember)
class NACDCBoardMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')

@admin.register(HousingCounselorContact)
class HousingCounselorContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email')


@admin.register(RebuildingTestimonial)
class RebuildingTestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'quote', 'created_at')
    search_fields = ('name', 'quote')
    ordering = ('-created_at',)


@admin.register(ILACImage)
class ILACImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'image')

@admin.register(SuggestionBoxMessage)
class SuggestionBoxMessageAdmin(admin.ModelAdmin):
    list_display = ('submission_type', 'created_at')
    list_filter = ('submission_type', 'created_at')
    ordering = ('-created_at',)
