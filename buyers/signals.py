from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Buyer


@receiver(post_save, sender=User)
def post_save_create_buyer(sender, instance, created, **kwargs):
    if created:
        Buyer.objects.create(user=instance)