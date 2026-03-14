from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string


# def send_test_email(request):
#     subject = "Welcome to my blog"
#     message = "This is a test email"
#     from_email = "nileshdeb500@gmail.com"
#     recipient_list = ["debnilesh69@gmail.com"]

#     send_mail(subject, message, from_email, recipient_list)
#     return HttpResponse("Email sent successfully")  
# Create your views here.

def send_test_email(request):
    subject = "Welcome to my blog"
    message = render_to_string("blog/welcome_email.html",{
        "name": "Nilesh",
        "course": "Django",
        "email": "nileshdeb500@gmail.com",
        "phone": "1234567890",
        "address": "1234567890",
        "city": "New York",
        "state": "NY",
        "zip": "10001",
        "country": "USA",
    })
    email = EmailMessage(subject, message, "nileshdeb500@gmail.com", ["debnilesh69@gmail.com"])
    email.content_subtype = "html"
    email.send()
    return HttpResponse("Email sent successfully")  