# Generated by Django 3.2.18 on 2024-01-17 23:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '__first__'),
        ('store', '0001_initial'),
        ('core', '0003_initial'),
        ('addons', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='helpful',
            field=models.ManyToManyField(blank=True, related_name='helpful', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='store.product'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productoffers',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_offer', to='store.product'),
        ),
        migrations.AddField(
            model_name='productoffers',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productfaq',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_faq', to='store.product'),
        ),
        migrations.AddField(
            model_name='productfaq',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productbidders',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_bidders', to='store.product'),
        ),
        migrations.AddField(
            model_name='productbidders',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='bidders',
            field=models.ManyToManyField(blank=True, related_name='bidders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_brand', to='store.brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='category', to='store.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendor', to='vendor.vendor'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_gallery', to='store.product'),
        ),
        migrations.AddField(
            model_name='cartorderitem',
            name='coupon',
            field=models.ManyToManyField(blank=True, to='vendor.Coupon'),
        ),
        migrations.AddField(
            model_name='cartorderitem',
            name='delivery_couriers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendor.deliverycouriers'),
        ),
        migrations.AddField(
            model_name='cartorderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.cartorder'),
        ),
        migrations.AddField(
            model_name='cartorderitem',
            name='product_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
        migrations.AddField(
            model_name='cartorderitem',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendor.vendor'),
        ),
        migrations.AddField(
            model_name='cartorder',
            name='billing_address_obj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.billingaddress'),
        ),
        migrations.AddField(
            model_name='cartorder',
            name='billing_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_country_field', to='addons.taxrate'),
        ),
        migrations.AddField(
            model_name='cartorder',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cartorder',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country_tax', to='addons.taxrate'),
        ),
        migrations.AddField(
            model_name='cartorder',
            name='coupons',
            field=models.ManyToManyField(blank=True, to='vendor.Coupon'),
        ),
        migrations.AddField(
            model_name='cartorder',
            name='vendor',
            field=models.ManyToManyField(blank=True, to='vendor.Vendor'),
        ),
    ]
