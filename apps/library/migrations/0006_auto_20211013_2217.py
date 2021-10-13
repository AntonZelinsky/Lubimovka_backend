# Generated by Django 3.2.7 on 2021-10-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20211013_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='authors_plays_links',
            new_name='author_plays_links',
        ),
        migrations.AlterField(
            model_name='author',
            name='other_links',
            field=models.ManyToManyField(blank=True, related_name='authors', to='library.OtherLink', verbose_name='Ссылки на внешние ресурсы'),
        ),
        migrations.AlterField(
            model_name='author',
            name='social_network_links',
            field=models.ManyToManyField(blank=True, related_name='authors', to='library.SocialNetworkLink', verbose_name='Ссылки на социальные сети'),
        ),
    ]
