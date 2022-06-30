# Generated by Django 3.2.13 on 2022-06-28 20:50

import apps.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20220622_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, unique=True, validators=[apps.core.validators.email_validator], verbose_name='Электронная почта'),
        ),
    ]