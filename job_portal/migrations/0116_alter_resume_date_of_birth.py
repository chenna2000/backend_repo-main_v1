# Generated by Django 5.1.4 on 2025-01-02 09:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0115_alter_achievements_publisher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
