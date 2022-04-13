# Generated by Django 4.0.3 on 2022-04-13 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_ratings_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='status',
            field=models.CharField(blank=True, choices=[('o', 'Side one'), ('t', 'Side two'), ('b', 'Bonus track'), ('e', 'Other')], default='0', help_text='Status', max_length=1),
        ),
    ]