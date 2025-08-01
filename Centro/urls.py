from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', user_views.register, name='register'),

    path('', user_views.home, name='home'),  # Home page

    path('about/', user_views.about, name='about'),

    path('donate/', user_views.donate, name='donate'),

    path('news/', user_views.news, name='news'),

    path('calendar/', user_views.calendar, name='calendar'),  

    path('team/', user_views.team, name='team'),

    path('contact/careers/', user_views.careers, name='careers'),
    path('contact/members/', user_views.members, name='members'),
    path('contact/privacy/', user_views.privacy, name='privacy'),
    path('contact/terms/', user_views.terms, name='terms'),

    path('forms/compliance/', user_views.compliance_view, name='compliance'),
    path('forms/compliance_success/', user_views.compliance_success_view, name='compliance_success'),

    path('forms/referral/', user_views.referral_view, name='referral_form'),
    path("forms/referral_success/", user_views.referral_success, name="referral_success"),

    path('forms/suggestions/', user_views.suggestion_box_view, name='suggestions'),
    path('forms/suggestions_success/', user_views.suggestions_success, name='suggestions_success'),


    path('programs/children/', user_views.children, name='children'),
    path('programs/community/', user_views.community, name='community'), 
    path('programs/family/', user_views.family, name='family'),
    path('programs/financial/', user_views.financial, name='financial'),
    path('programs/food/', user_views.food, name='food'),
    path('programs/foster/', user_views.foster, name='foster'),
    path('programs/homeowner/', user_views.homeowner, name='homeowner'),
    path('programs/ilac/', user_views.ilac, name='ilac'),
    path('programs/nacdc/', user_views.nacdc, name='nacdc'),
    path('programs/rebuild/', user_views.rebuild, name='rebuild'),


    path('forms/', user_views.forms, name='forms'),

    path('contact/success/', user_views.contact_success_view, name='contact_success'),
    path('contact/', user_views.contact_view, name='contact'),

    path('subscribe/', user_views.subscribe_view, name='subscribe'),
    path('subscribe_success/', user_views.subscribe_success_view, name='subscribe_success'),

    path("admin/", admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)