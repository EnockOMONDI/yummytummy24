# Generated by Django 3.2.18 on 2023-04-11 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0013_auto_20230410_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='paypal_email_address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
