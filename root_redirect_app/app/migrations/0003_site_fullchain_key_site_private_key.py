# Generated by Django 4.1.2 on 2022-10-19 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_site_source_url_alter_site_target_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='fullchain_key',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='private_key',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]