# Generated by Django 5.0.4 on 2025-02-12 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wg_blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="excerpt",
            field=models.TextField(blank=True),
        ),
    ]
