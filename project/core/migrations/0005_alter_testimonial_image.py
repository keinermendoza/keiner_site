# Generated by Django 5.0.4 on 2024-06-04 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_testimonial_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testimonial",
            name="image",
            field=models.FileField(blank=True, null=True, upload_to="testimonials"),
        ),
    ]
