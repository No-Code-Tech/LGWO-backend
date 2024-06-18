# Generated by Django 5.0.2 on 2024-04-13 08:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('contact_manager_name', models.CharField(max_length=100)),
                ('contact_manager_email', models.EmailField(max_length=100)),
                ('contact_manager_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CasualOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('medium', models.CharField(max_length=100)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.client')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signed_date', models.DateField(auto_now_add=True)),
                ('expiry_date', models.DateField()),
                ('is_terminated', models.BooleanField(default=False)),
                ('is_terminate_date', models.DateField(blank=True, null=True)),
                ('termination_reason', models.TextField(blank=True, null=True)),
                ('document', models.FileField(upload_to='contract')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contracts', to='client.client')),
            ],
        ),
    ]
