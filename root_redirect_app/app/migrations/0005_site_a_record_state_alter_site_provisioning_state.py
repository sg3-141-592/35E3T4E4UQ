# Generated by Django 4.1.2 on 2022-10-20 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_site_provisioning_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='a_record_state',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='site',
            name='provisioning_state',
            field=models.CharField(choices=[('1-GET-USER-URL', '1 - Get user urls'), ('2-ADD-A-RECORD', '2 - Add A record'), ('3-CHECK-A-RECORD', '3 - Checking A record mapping'), ('4-GENERATE-CERT', '4 - Generating certificate'), ('5-TEST-CERT', '5 - Testing SSL certificate'), ('6-TEST-REDIRECT', '6 - Testing redirect'), ('VALID', 'Valid entry')], default='1-GET-USER-URL', max_length=32),
        ),
    ]
