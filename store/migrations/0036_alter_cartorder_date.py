# Generated by Django 3.2.18 on 2023-04-06 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0035_remove_gallery_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
