# Generated by Django 2.2.7 on 2019-11-16 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myScoreboard', '0004_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='flags_gotten',
            field=models.ManyToManyField(to='myScoreboard.flag'),
        ),
    ]
