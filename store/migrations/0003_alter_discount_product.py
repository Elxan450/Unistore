# Generated by Django 4.2.2 on 2023-07-17 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_battery_display_graphics_harddrive_manufacturer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discount', to='store.product'),
        ),
    ]
