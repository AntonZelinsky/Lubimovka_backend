# Generated by Django 3.2.12 on 2022-02-20 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20220220_2205'),
        ('library', '0005_alter_performancemediareview_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='play',
            options={'permissions': (('can_publish_play', 'Может опубликовать пьесу'),), 'verbose_name': 'Пьеса', 'verbose_name_plural': 'Пьесы'},
        ),
        migrations.RemoveField(
            model_name='play',
            name='is_draft',
        ),
        migrations.AddField(
            model_name='play',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.status', verbose_name='Статус'),
        ),
    ]
