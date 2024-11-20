from django.contrib import admin
from .models import ContactMessage
from django.contrib import admin
from .models import ComplianceMessage
from .models import Referral
from .models import Subscriber



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