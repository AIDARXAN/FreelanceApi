from decimal import Decimal

from django.db.models import F
from rest_framework import status
from rest_framework.response import Response

from billing.models import TransactionsLog
from task.models import User


class Transaction:
    def task_completed_transaction(user, money, task):
        log_params = {'user': user, 'task': task, 'difference': money}
        current_balance = User.objects.get(id=user.id).balance
        log_params['old_balance'] = current_balance
        log_params['new_balance'] = current_balance + Decimal(money)

        TransactionsLog.objects.get_or_create(**log_params)

        User.objects.select_for_update().filter(id=user.id).update(balance=F('balance') + Decimal(money))

    def task_created_transaction(user, money):
        log_params = {'user': user}
        current_balance = User.objects.get(id=user.id).balance
        log_params['old_balance'] = current_balance

        if log_params['old_balance'] > Decimal(money):
            log_params['difference'] = Decimal(money) * (-1)
            log_params['new_balance'] = current_balance - Decimal(money)
            TransactionsLog.objects.get_or_create(**log_params)
            User.objects.select_for_update().filter(id=user.id).update(balance=F('balance') - Decimal(money))

            return Response({'message': 'Task created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Amount of money on your balance is lower then the task price'},
                            status=status.HTTP_402_PAYMENT_REQUIRED)
