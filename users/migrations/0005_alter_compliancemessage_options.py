# Generated by Django 5.0.1 on 2024-11-20 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_compliancemessage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compliancemessage',
            options={'verbose_name': 'Compliance Form', 'verbose_name_plural': 'Compliance Forms'},
        ),
    ]
