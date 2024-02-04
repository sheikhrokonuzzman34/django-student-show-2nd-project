from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, max_length=1)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    profile_image = models.ImageField(
        upload_to='profile', default='no_profile.jpg')
    address = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = 'UserProfiles'

    def __str__(self):
        return self.user.username
