# Generated by Django 4.2.11 on 2024-03-24 10:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='links',
            name='link_url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]