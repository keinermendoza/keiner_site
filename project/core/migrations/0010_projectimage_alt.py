# Generated by Django 5.0.6 on 2024-06-30 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_project_image_alter_testimonial_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='alt',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
