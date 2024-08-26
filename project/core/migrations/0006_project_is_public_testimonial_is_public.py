# Generated by Django 5.0.4 on 2024-06-13 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_testimonial_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="is_public",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="testimonial",
            name="is_public",
            field=models.BooleanField(default=False),
        ),
    ]
