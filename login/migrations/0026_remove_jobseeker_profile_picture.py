# Generated by Django 5.1.4 on 2025-01-07 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0025_jobseeker_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseeker',
            name='profile_picture',
        ),
    ]
