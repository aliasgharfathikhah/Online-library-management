from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    nationalid = models.CharField(max_length = 255)
    City = models.CharField(max_length = 255)
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('male', 'مرد') ,
        ('female', 'زن'),
    ]
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
    dateOfMembership = models.TimeField(auto_now_add = True)

    def __str__(self):
        return self.name