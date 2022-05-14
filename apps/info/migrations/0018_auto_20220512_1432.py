# Generated by Django 3.2.12 on 2022-05-12 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_data_additional_and_updated_email_settings'),
        ('info', '0017_auto_20220429_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='festival',
            name='images',
        ),
        migrations.CreateModel(
            name='FestivalImage',
            fields=[
                ('image_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.image')),
                ('festival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='info.festival', verbose_name='Изображения фестиваля')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.image',),
        ),
    ]
