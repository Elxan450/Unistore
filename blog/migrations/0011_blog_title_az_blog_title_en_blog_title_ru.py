# Generated by Django 4.2.2 on 2023-10-06 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blog_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title_az',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
    ]
