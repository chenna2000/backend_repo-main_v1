# Generated by Django 5.1.4 on 2025-01-07 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0131_remove_college_profile_picture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker_resume',
            name='profile_picture',
            field=models.ImageField(default='Unknown', upload_to='profile_pics/'),
        ),
    ]
