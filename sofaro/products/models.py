
from decimal import Decimal

from django.conf import settings
from django.db import models



# class Product(models.Model):
#     external_id = models.CharField(max_length=255, blank=True, null=True)
#     title = models.CharField(max_length=255)
#     image = models.ImageField(upload_to="products/", blank=True, null=True)
#     price = models.DecimalField(default=Decimal("0"), decimal_places=5, max_digits=10)
#     price_usd = models.DecimalField(default=Decimal("0"), decimal_places=5, max_digits=10)
#     excerpt = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(
#         auto_now_add=True, db_index=True
#     )

# Create your models here.
