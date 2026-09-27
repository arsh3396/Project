from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_description = models.CharField()
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTouJqFpAlcO1WK_3LKKl64xaEiQkjgx5YAv6pcM8l2sg&s=10")
    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return reverse("myapp:index")
    
