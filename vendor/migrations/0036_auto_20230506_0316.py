# Generated by Django 3.2.18 on 2023-05-06 02:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor', '0035_coupon_get_percent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='get_percent',
        ),
        migrations.AddField(
            model_name='coupon',
            name='redemption',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coupon',
            name='used_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coupon_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
