# Generated by Django 5.0.4 on 2024-06-03 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="status",
            field=models.CharField(
                choices=[("E", "Editing"), ("P", "Published")],
                default="E",
                max_length=1,
            ),
        ),
    ]
