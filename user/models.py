from decimal import Decimal
from math import fabs

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import F


class User(AbstractUser):
    CUSTOMER = '1'
    EXECUTOR = '2'

    USER_GROUP_CHOICES = (
        (CUSTOMER, 'customer'),
        (EXECUTOR, 'executor'),
    )

    group = models.CharField(max_length=20, choices=USER_GROUP_CHOICES)
    balance = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

