from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        UNSET = 'MF', 'Unset'

    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.UNSET)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    countery = models.CharField(blank=True,max_length =40 )
    city = models.CharField(blank=True ,max_length =40)
    postcode = models.IntegerField(blank=True, null=True)