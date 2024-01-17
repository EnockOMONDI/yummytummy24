# Generated by Django 3.2.18 on 2023-04-19 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0060_auto_20230418_2200'),
        ('vendor', '0023_alter_payouttracker_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.cartorder'),
        ),
    ]
