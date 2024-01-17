# Generated by Django 3.2.18 on 2023-04-24 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('addons', '0022_taxrate_custom_name'),
        ('vendor', '0026_notification_seen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='postal_code',
        ),
        migrations.AddField(
            model_name='vendor',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='vendor_followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vendor',
            name='keywords',
            field=models.CharField(default=1, help_text='Add keywords related to your shop, this would help buyers locate your shop', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor',
            name='shop_policy',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='notification',
            name='type',
            field=models.CharField(choices=[('new_order', 'New Order'), ('new_offer', 'New Offer'), ('new_bidding', 'New Bidding'), ('item_arrived', 'Item Arrived'), ('item_shipped', 'Item Shipped'), ('item_delivered', 'Item Delivered'), ('tracking_id_added', 'Tracking ID Added'), ('tracking_id_changed', 'Tracking ID Changed'), ('offer_rejected', 'Offer Rejected'), ('offer_accepted', 'Offer Accepted'), ('product_published', 'Product Published'), ('product_rejected', 'Product Rejected'), ('product_disabled', 'Product Disabled')], default='new_order', max_length=100),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendor_country', to='addons.taxrate'),
        ),
    ]
