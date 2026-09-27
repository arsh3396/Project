from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Item(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['user_name', 'item_price']),
        ]
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200, db_index=True)
    item_description = models.CharField()
    item_price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    item_image = models.URLField(max_length=1000, default="https://placeholder.com")
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return reverse("myapp:index")
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    added_on = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name