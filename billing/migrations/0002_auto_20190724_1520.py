# Generated by Django 2.2.2 on 2019-07-24 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Balance',
        ),
        migrations.DeleteModel(
            name='LogTransaction',
        ),
    ]