# Generated by Django 3.2.9 on 2021-11-29 16:41

from django.db import migrations


def add_short_list_program(apps, schema_editor):
    Program = apps.get_model('library', 'ProgramType')
    Program.objects.create(
        name="Шорт-лист",
        slug="short-list"
    )


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_programtype_slug'),
    ]

    operations = [migrations.RunPython(add_short_list_program)]