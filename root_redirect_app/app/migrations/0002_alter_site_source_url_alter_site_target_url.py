# Generated by Django 4.1.2 on 2022-10-18 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='source_url',
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='site',
            name='target_url',
            field=models.CharField(max_length=2048),
        ),
    ]
