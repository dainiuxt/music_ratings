# Generated by Django 4.0.3 on 2022-04-14 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_ratings_api', '0002_song_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='field_duration',
            field=models.DurationField(null=True),
        ),
    ]