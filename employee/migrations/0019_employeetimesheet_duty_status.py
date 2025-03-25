# Generated by Django 5.0.2 on 2025-03-21 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0018_employeetimesheet_verification_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeetimesheet',
            name='duty_status',
            field=models.CharField(blank=True, choices=[('ABSENT', 'Absent'), ('SICK', 'Sick'), ('LEAVE', 'Leave')], max_length=10, null=True),
        ),
    ]
