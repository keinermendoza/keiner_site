# Generated by Django 5.0.6 on 2024-06-30 00:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_project_tecnologies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='testimonials'),
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_images')),
                ('device', models.CharField(choices=[('M', 'Mobile'), ('D', 'Desktop')], default='D', max_length=1)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.project')),
            ],
        ),
    ]
