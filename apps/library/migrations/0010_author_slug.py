# Generated by Django 3.2.12 on 2022-03-03 18:16

from django.db import migrations, models
from apps.core import utils

def set_slug(apps, schema_editor):
    Author = apps.get_model("library", "Author")
    qs = Author.objects.all()
    for author in qs:
        author.slug = utils.slugify(author.person.full_name)
        author.save()

class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20220226_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, help_text='Если не заполнено, будет сформировано автоматически', verbose_name='Транслит фамилии для формирования адресной строки'),
        ),
        migrations.RunPython(
            set_slug
        ),
    ]
