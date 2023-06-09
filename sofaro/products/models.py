
from decimal import Decimal

from django.conf import settings
from django.db import models

COUNTRY_CHOICES = (
    ("Турция", "ТУРЦИЯ"),
    ("ОАЭ", "ОАЭ"),
    ("Египет", "ЕГИПЕТ"),
    ("Греция", "ГРЕЦИЯ")
)

class Product(models.Model):
    external_id = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)
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
    
    def get_score(self):
        scores = [score.value for score in self.scores.all()]
        if scores:
           return sum(scores) / len(scores)
        return 0
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/")
    

    def __str__(self):
        return f"ProductImage: {self.image} - {self.product}"  

class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="purchases"
    )
 
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="purchases"
    )
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"Booking: {self.user} - {self.product} - {self.count}"

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

class Comment(models.Model):
    post = models.ForeignKey(Product,  
			     on_delete=models.CASCADE,  
			     related_name='comments',
                 )  
    name = models.CharField(max_length=80)  
    email = models.EmailField()  
    body = models.TextField()  
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  
    active = models.BooleanField(default=True)  
      
    class Meta:  
        ordering = ('created',)  
          
    def __str__(self):  
        return 'Comment by {} on {}'.format(self.name, self.post)
    
class Score(models.Model):
    post = models.ForeignKey(
        Product,  
        on_delete=models.CASCADE,  
        related_name='scores',
    )
    value = models.IntegerField()

    def __str__(self):
        return f"{self.post.title} {self.value}"
