from django.db import models
from task.models import User


class TransactionsLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey('task.Task', on_delete=models.CASCADE, default=None, null=True)
    date = models.DateTimeField(auto_now_add=True)
    old_balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    new_balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    difference = models.DecimalField(max_digits=8, decimal_places=2, default=0)