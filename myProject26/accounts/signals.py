from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        print(f"New user registered: {instance.username}")

        subject = "Welcome to our website"
        message = f"Welcome to our website, {instance.username}! Thank you for registering."
        from_email = "nileshdeb500@gmail.com"
        recipient_list = [instance.email]

        send_mail(subject, message, from_email, recipient_list,fail_silently=False)
        print(f"Welcome email sent Successfully")