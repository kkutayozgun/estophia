# Generated by Django 3.2 on 2022-07-10 11:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('female', '0025_auto_20220710_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='femaleblogtranslation',
            name='banner_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Banner Description'),
        ),
    ]