# Generated by Django 4.2.2 on 2023-08-23 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_productreview_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productversion',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
