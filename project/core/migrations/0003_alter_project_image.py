# Generated by Django 5.0.4 on 2024-06-03 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_project_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.FileField(blank=True, null=True, upload_to="projects"),
        ),
    ]
