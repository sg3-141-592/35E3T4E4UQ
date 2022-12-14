# Generated by Django 4.1.2 on 2022-10-20 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_site_fullchain_key_site_private_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='provisioning_state',
            field=models.CharField(choices=[('1-GET-USER-URL', 'Get user urls'), ('2-ADD-A-RECORD', 'Add A record'), ('3-CHECK-A-RECORD', 'Checking A record mapping'), ('4-GENERATE-CERT', 'Generating certificate'), ('5-TEST-CERT', 'Testing SSL certificate'), ('6-TEST-REDIRECT', 'Testing redirect'), ('VALID', 'Valid entry')], default='1-GET-USER-URL', max_length=32),
        ),
    ]
