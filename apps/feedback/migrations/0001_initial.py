# Generated by Django 3.2.12 on 2022-04-22 12:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('question', models.TextField(max_length=500, validators=[django.core.validators.MinLengthValidator(2, 'Вопрос должен состоять более чем из 2 символов')], verbose_name='Текст вопроса')),
                ('author_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('author_email', models.EmailField(max_length=50, verbose_name='Электронная почта')),
                ('sent', models.BooleanField(default=False, verbose_name='Отправлено')),
            ],
            options={
                'verbose_name': 'Вопрос или предложение',
                'verbose_name_plural': 'Вопросы или предложения',
            },
        ),
    ]
