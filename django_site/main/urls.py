from django.urls import path, include
from . import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path('', views.create_appointment, name='home'),
    path('about', views.about, name='about'),
    path('thanks', views.thanks, name='thanks'),
]