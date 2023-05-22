from django.db import models

from decimal import Decimal

from django.conf import settings
from django.db import models



class Users(models.Model):
    user = models.OneToOneField(
    settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    age = models.IntegerField(default=18)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )

# Create your models here.
