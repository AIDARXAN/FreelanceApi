from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    customer = models.ForeignKey(User, related_name='customer', on_delete=models.CASCADE)
    executor = models.ForeignKey(User, related_name='executor', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    accomplished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

