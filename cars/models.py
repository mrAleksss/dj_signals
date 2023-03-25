from django.db import models
from buyers.models import Buyer
import uuid


class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    code = models.CharField(max_length=10, blank=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.name}-{self.price}-{self.buyer}"


    # def save(self, *args, **kwargs):
    #     if self.code == "":
    #         self.code = str(uuid.uuid4()).replace("-", "").upper()[:10]
    #     return super().save(*args, **kwargs)


