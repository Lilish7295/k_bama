from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, on__delete=models.CASCADE)
    province = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    is_superuser = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    

    