from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Blog


# Triggered before saving a Blog instance
@receiver(post_save, sender=Blog)
def before_blog_save(sender, instance, created, **kwargs):
    print(f'About to save blog [Pre-Save]:{instance.title}')


# Triggered after saving a Blog instance
@receiver(post_save, sender=Blog)
def after_blog_save(sender, instance, created, **kwargs):
    if created:
        print(f'Blog created: {instance.title}')
    else:
        print(f'Blog updated: {instance.title}')