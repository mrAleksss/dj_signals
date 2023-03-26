from django.dispatch import receiver
from .models import Sale
from orders.models import Order
from django.db.models.signals import pre_delete


@receiver(pre_delete, sender=Sale)
def delete_sale_and_change_order(sender, instance, **kwargs):
    obj = instance.order
    obj.active = False
    obj.save()