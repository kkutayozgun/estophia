# Generated by Django 3.2 on 2022-06-29 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('female', '0020_auto_20220629_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='femaleservicecategory',
            name='banner_image',
            field=models.ImageField(blank=True, null=True, upload_to='service/category/banner', verbose_name='Banner Görseli'),
        ),
        migrations.AlterField(
            model_name='femaleservicecategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='service/category', verbose_name='Kategori Görseli'),
        ),
    ]