# Generated by Django 4.2.15 on 2024-10-08 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0075_remove_studentenquiry_password_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='achievements',
            old_name='date_of_issue',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='publications',
            old_name='date_of_publications',
            new_name='end_date',
        ),
        migrations.AddField(
            model_name='achievements',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='description',
            field=models.TextField(default='No description'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_link',
            field=models.TextField(default=list),
        ),
        migrations.AddField(
            model_name='publications',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
