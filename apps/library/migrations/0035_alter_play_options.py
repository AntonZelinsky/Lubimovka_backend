# Generated by Django 3.2.13 on 2022-07-25 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0034_alter_programtype_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='play',
            options={'ordering': ('name',), 'verbose_name': 'Пьеса', 'verbose_name_plural': 'Пьесы'},
        ),
    ]