# Generated by Django 5.1 on 2025-03-01 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0012_remove_postimage_post_delete_post_delete_postimage"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Topic",
        ),
    ]
