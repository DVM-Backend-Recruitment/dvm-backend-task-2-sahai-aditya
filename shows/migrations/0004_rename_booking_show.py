# Generated by Django 5.1.3 on 2024-11-16 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_booking'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booking',
            new_name='Show',
        ),
    ]
