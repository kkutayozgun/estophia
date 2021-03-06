# Generated by Django 3.2 on 2022-06-27 19:38

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('male', '0014_auto_20220626_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaleContactPageSeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image', models.ImageField(blank=True, null=True, upload_to='contact/', verbose_name='Banner Image')),
                ('meta_keywords', models.ManyToManyField(blank=True, to='common.Keywords', verbose_name='Meta Anahtar Kelimeler')),
            ],
            options={
                'verbose_name': 'Contact Page SEO',
                'verbose_name_plural': 'Contact Page SEO',
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MaleContactPageSeoTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('seo_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='SEO Başlığı')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Meta Açıklaması')),
                ('banner_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Banner Title')),
                ('banner_description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Banner Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='male.malecontactpageseo')),
            ],
            options={
                'verbose_name': 'Contact Page SEO Translation',
                'db_table': 'male_malecontactpageseo_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
