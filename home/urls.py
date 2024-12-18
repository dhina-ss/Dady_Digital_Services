from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-form/', views.contact_form_view, name='contact'),
    path('subscribe-form/', views.subscribe_form_view, name='subscribe'),
]
