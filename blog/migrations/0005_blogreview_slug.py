# Generated by Django 4.2.2 on 2023-08-23 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogreview',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
