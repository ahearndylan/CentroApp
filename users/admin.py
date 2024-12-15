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