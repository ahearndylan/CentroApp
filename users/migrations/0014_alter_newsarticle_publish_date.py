# Generated by Django 5.0.1 on 2025-06-03 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_newsarticle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='publish_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
