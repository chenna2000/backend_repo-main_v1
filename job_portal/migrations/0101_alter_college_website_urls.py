# Generated by Django 5.1.2 on 2024-11-05 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0100_alter_company_website_urls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='website_urls',
            field=models.CharField(default='Unknown', max_length=500),
        ),
    ]
