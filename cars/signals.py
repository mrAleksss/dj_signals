from .models import Car
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
import uuid
from buyers.models import Buyer


@receiver(pre_save, sender=Car)
def create_code_mode_buyer_pre_save(sender, instance, **kwargs):
    if instance.code == "":
        instance.code = str(uuid.uuid4()).replace("-", "").upper()[:10]
    
    obj = Buyer.objects.get(user=instance.buyer.user)
    obj.from_signal = True
    obj.save()