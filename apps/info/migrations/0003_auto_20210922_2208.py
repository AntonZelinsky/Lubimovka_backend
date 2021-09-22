# Generated by Django 3.2.7 on 2021-09-22 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_rename_partners_partner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(max_length=200, unique=True, verbose_name='Текст вопроса')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.AddField(
            model_name='partner',
            name='picture',
            field=models.ImageField(default=1, upload_to='info/', verbose_name='Логотип'),
            preserve_default=False,
        ),
    ]
