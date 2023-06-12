
from decimal import Decimal

from django.conf import settings
from django.db import models


COUNTRY_CHOICES = (
    ("Турция", "ТУРЦИЯ"),
    ("Оаэ", "ОАЭ"),
    ("Египет", "ЕГИПЕТ"),
    ("Греция", "ГРЕЦИЯ")
)


class Product(models.Model):
    external_id = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    country = models.CharField(max_length=32, choices=COUNTRY_CHOICES, default= "Турция")
    price = models.DecimalField(default=Decimal("0"), decimal_places=5, max_digits=10)
    price_usd = models.DecimalField(default=Decimal("0"), decimal_places=5, max_digits=10)
    excerpt = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )

    def __str__(self):
        return f"Product: {self.title} - {self.price}"
    

class Purchase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="purchases"
    )
 
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="purchases"
    )
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"Purchase: {self.user} - {self.product} - {self.count}"



class Hotels(models.Model):
    external_id = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=32, choices=COUNTRY_CHOICES, default= "Турция")
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    excerpt = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )

    def __str__(self):
        return f"Hotels: {self.title} - {self.country}"
    

# class OneHotel(models.Model):
#     external_id = models.CharField(max_length=255, blank=True, null=True)
#     title = models.CharField(max_length=255)
#     image = models.ImageField(upload_to="products/", blank=True, null=True)
#     country = models.CharField(max_length=32, choices=COUNTRY_CHOICES, default= "Турция")
#     price = models.DecimalField(default=Decimal("0"), decimal_places=5, max_digits=10)
#     price_usd = models.DecimalField(default=Decimal("0"), decimal_places=5, max_digits=10)
#     excerpt = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(
#         auto_now_add=True, db_index=True
#     )

#     def __str__(self):
#         return f"Product: {self.title} - {self.price}"