# Generated by Django 4.1.6 on 2023-02-28 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todaysong', '0002_song_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_sent',
            field=models.BooleanField(default=False),
        ),
    ]
