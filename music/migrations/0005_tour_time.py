# Generated by Django 2.2.3 on 2020-02-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20200216_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='time',
            field=models.TimeField(default='20:00'),
        ),
    ]