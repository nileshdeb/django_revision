from django.shortcuts import render
from django.core.mail import send_mass_mail
from django.http import HttpResponse


def send_bulk_email(request):
    messages1=('welcome user 1' )
    messages2=('welcome user 2' )

    send_mass_mail((
        messages1,messages2
         
    ),fail_silently=False)
    return HttpResponse("Email sent successfully")
# Create your views here.
