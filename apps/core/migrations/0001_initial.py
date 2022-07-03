# Generated by Django 3.2.11 on 2022-01-29 14:40

from django.db import migrations, models

import apps.core.validators
from apps.core.models import Setting


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(help_text='Загрузите фотографию', upload_to='images/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50, validators=[apps.core.validators.name_validator], verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, validators=[apps.core.validators.name_validator], verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=50, validators=[apps.core.validators.name_validator], verbose_name='Отчество')),
                ('city', models.CharField(blank=True, help_text='Обязательно указать для: членов команды, волонтёров и авторов.', max_length=50, verbose_name='Город проживания')),
                ('email', models.EmailField(blank=True, help_text='Обязательно указать для: членов команды, волонтёров и авторов.', max_length=200, null=True, unique=True, verbose_name='Электронная почта')),
                ('image', models.ImageField(blank=True, help_text='Обязательно указать для: членов команды, спонсоров и волонтёров.', upload_to='images/person_avatars', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Люди',
                'ordering': ('last_name',),
            },
        ),
        migrations.CreateModel(
            name='RoleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_type', models.CharField(choices=[('blog_persons_role', 'Роль в блоге'), ('performanse_role', 'Роль в спектаклях'), ('play_role', 'Роль в пьесах'), ('master_class_role', 'Роль в мастер классах'), ('reading_role', 'Роль в читках')], default='blog_persons_role', help_text='Укажите, где будет использована роль', max_length=20, unique=True, verbose_name='Тип роли')),
            ],
            options={
                'verbose_name': 'Тип роли',
                'verbose_name_plural': 'Типы ролей',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('group', models.CharField(choices=[('EMAIL', 'Почта'), ('MAIN', 'Главная'), ('FIRST_SCREEN', 'Первая страница'), ('GENERAL', 'Общие'), ('AFISHA', 'Афиша')], default='GENERAL', max_length=50, verbose_name='Группа настроек')),
                ('field_type', models.CharField(choices=[('BOOLEAN', 'Да/Нет'), ('TEXT', 'Текст'), ('URL', 'URL'), ('IMAGE', 'Картинка'), ('EMAIL', 'EMAIL')], max_length=40, verbose_name='Выбор поля настроек')),
                ('settings_key', models.SlugField(max_length=40, unique=True, verbose_name='Ключ настройки')),
                ('description', models.TextField(blank=True, max_length=250, verbose_name='Описание настройки')),
                ('boolean', models.BooleanField(default=False, verbose_name='Да или Нет')),
                ('text', models.TextField(blank=True, max_length=500, verbose_name='Текст')),
                ('url', models.URLField(blank=True, verbose_name='Ссылка')),
                ('image', models.ImageField(blank=True, upload_to='core/', verbose_name='Изображение')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Общие настройки',
                'verbose_name_plural': 'Общие настройки',
                'ordering': ('group', 'settings_key'),
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('name_plural', models.CharField(max_length=50, unique=True, verbose_name='Название во множественном числе')),
                ('slug', models.SlugField(help_text='Заполняется автоматически', max_length=60, unique=True, verbose_name='Код-имя латиницей')),
                ('types', models.ManyToManyField(related_name='type_roles', to='core.RoleType', verbose_name='Типы ролей')),
            ],
            options={
                'verbose_name': 'Должность/позиция',
                'verbose_name_plural': 'Должности/позиции',
                'ordering': ('name',),
            },
        ),
        migrations.AddConstraint(
            model_name='person',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name', 'middle_name', 'email'), name='unique_person'),
        ),
    ]
