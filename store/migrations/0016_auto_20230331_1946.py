# Generated by Django 3.2.18 on 2023-04-01 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20230331_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='shipping',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AddField(
            model_name='cartorder',
            name='vat',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]
