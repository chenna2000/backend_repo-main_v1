# Generated by Django 5.1.4 on 2025-01-07 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0129_remove_jobseeker_resume_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker_resume',
            name='Attachment',
            field=models.FileField(default='Unknown', upload_to='attachments/'),
        ),
    ]
