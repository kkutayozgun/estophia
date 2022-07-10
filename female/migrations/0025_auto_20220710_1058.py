# Generated by Django 3.2 on 2022-07-10 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('female', '0024_femalesearchpageseo_femalesearchpageseotranslation'),
    ]

    operations = [
        migrations.AddField(
            model_name='femaleservicecategory',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='service/category/icons', verbose_name='Kategori İconu'),
        ),
        migrations.AddField(
            model_name='femaleservicecategory',
            name='in_home',
            field=models.BooleanField(default=True, verbose_name='Anasayfa servisler içerisinde mi?'),
        ),
    ]