# Generated by Django 5.0.1 on 2024-11-20 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_referral'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Referral',
        ),
    ]
