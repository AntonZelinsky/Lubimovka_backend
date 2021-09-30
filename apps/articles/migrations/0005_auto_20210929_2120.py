# Generated by Django 3.2.7 on 2021-09-29 21:20

import apps.articles.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('articles', '0004_auto_20210927_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='files')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='images')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('order', apps.articles.fields.OrderField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='articles.project')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='BlockText',
        ),
        migrations.DeleteModel(
            name='BlockTitle',
        ),
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['order']},
        ),
        migrations.RemoveField(
            model_name='content',
            name='created',
        ),
        migrations.RemoveField(
            model_name='content',
            name='description',
        ),
        migrations.RemoveField(
            model_name='content',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='content',
            name='name',
        ),
        migrations.RemoveField(
            model_name='content',
            name='project',
        ),
        migrations.AddField(
            model_name='content',
            name='order',
            field=apps.articles.fields.OrderField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.ForeignKey(limit_choices_to={'model__in': ('text', 'video', 'image', 'file')}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='content',
            name='module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='articles.module'),
            preserve_default=False,
        ),
    ]