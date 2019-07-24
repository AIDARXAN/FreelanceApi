# Generated by Django 2.2.2 on 2019-07-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_logtransaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='logtransaction',
            name='credit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='logtransaction',
            name='debit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]