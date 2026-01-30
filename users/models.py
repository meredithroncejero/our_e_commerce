from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Product(models.Model):
        name = models.CharField(max_length=150)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        description = models.TextField(blank=True)
        stock = models.IntegerField(default=0)
        is_active = models.BooleanField(default=True)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.name
