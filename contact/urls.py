from django.urls import path
from . import views


urlpatterns = [
    path('contacted', views.get_contact, name='contacted'),
]
