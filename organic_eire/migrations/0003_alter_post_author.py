# Generated by Django 4.2.11 on 2024-03-15 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organic_eire', '0002_post_author_post_content_post_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organic_eire_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
