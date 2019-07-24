from decimal import Decimal
from math import fabs

from django.db import models
from django.db.models import F

from task.models import User


class Balance(models.Model):
    def update_balance(user, money, task):
        log_filter = {'user': user, 'task': task}
        current_balance = User.objects.get(id=user.id).balance
        log_filter['balance'] = current_balance + Decimal(money)

        LogTransaction.objects.get_or_create(**log_filter)

        User.objects.select_for_update().filter(id=user.id).update(balance=F('balance') + Decimal(money))


class LogTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey('task.Task', on_delete=models.CASCADE, default=None, null=True)
    date = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0)
