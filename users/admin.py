from django.contrib import admin
from .models import ContactMessage
from django.contrib import admin
from .models import ComplianceMessage
from .models import Referral
from .models import Subscriber
from .models import CalendarImage, CalendarEvent
from .models import Donor



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
