from locale import normalize
from this import d
from django.db import models
from django.contrib.auth.models import User


class UserInterest(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class UserPersona(
    models.Model
):  # systems generated, generate as a webwsite administrator
    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Create your models here.
class UserProfile(models.Model):
    # owner (foreign key -> references another table profile)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    # settings
    is_full_name_displayed = models.BooleanField(
        default=True
    )  # create model want property call is_full_name_displayed

    # details
    bio = models.CharField(max_length=500, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    persona = models.ForeignKey(
        UserPersona, on_delete=models.SET_NULL, blank=True, null=True
    )  # Foreign key
    interest = models.ManyToManyField(UserInterest, blank=True)
