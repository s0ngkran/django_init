from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    choice_sex = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    sex = models.CharField(max_length=255, choices=choice_sex, null=True, blank=True)
    height = models.IntegerField(default=0, null=True, blank=True)
    weight = models.IntegerField(default=0, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
class Hand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='hand', null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    