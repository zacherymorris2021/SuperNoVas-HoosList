# Generated by Django 2.1.7 on 2019-10-27 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='bad_votes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='seller',
            name='good_votes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='seller',
            name='num_transactions',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
