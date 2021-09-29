# Generated by Django 3.2.7 on 2021-09-21 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('type', models.CharField(choices=[(1, 'Генеральный партнер'), (2, 'Партнер фестиваля'), (3, 'Информационный партнер')], max_length=2, verbose_name='Тип')),
                ('url', models.URLField(verbose_name='Ссылка на сайт')),
                ('image', models.CharField(max_length=200, verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
    ]