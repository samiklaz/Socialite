# Generated by Django 3.0.7 on 2020-06-13 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0003_auto_20200613_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follower',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=models.IntegerField(default=0),
        ),
    ]
