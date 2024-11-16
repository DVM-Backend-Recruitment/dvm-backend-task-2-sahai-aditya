# Generated by Django 5.1.3 on 2024-11-16 18:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0002_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('vacant_seats', models.SmallIntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows.movie')),
                ('theatre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shows.theatre')),
            ],
        ),
    ]
