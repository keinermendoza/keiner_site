# Generated by Django 5.0.6 on 2024-06-30 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_projectimage_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='video_demo',
            field=models.URLField(blank=True, null=True),
        ),
    ]
