# Generated by Django 5.0.7 on 2024-07-26 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reco_app', '0004_adviser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adviser',
            name='number_of_advisees',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='is_active',
        ),
    ]