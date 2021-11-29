from django.db import models   
from django.contrib.auth.models import User

# Create your models here.
class userProfile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    avatar=models.ImageField(null=True, blank=True)
    