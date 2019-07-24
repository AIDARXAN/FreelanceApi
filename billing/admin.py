from django.contrib import admin

from billing.models import Balance, LogTransaction

admin.site.register(Balance)
admin.site.register(LogTransaction)