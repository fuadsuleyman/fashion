# Generated by Django 3.1.4 on 2020-12-23 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='image',
            field=models.ImageField(upload_to='logo', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='parallaxbanner',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='slide_image', verbose_name='Slide Imahe'),
        ),
    ]
