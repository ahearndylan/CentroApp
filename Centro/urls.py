from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views

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

    # Contact pages
    path('contact/careers/', user_views.careers, name='careers'),
    path('contact/members/', user_views.members, name='members'),
    path('contact/privacy/', user_views.privacy, name='privacy'),
    path('contact/terms/', user_views.terms, name='terms'),

    # Forms pages
    path('forms/compliance/', user_views.compliance, name='compliance'),
    path('forms/referral/', user_views.referral, name='referral'),

    # Program pages
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

    path('contact/', user_views.contact, name='contact'),

    path('forms/', user_views.forms, name='forms'),


]
