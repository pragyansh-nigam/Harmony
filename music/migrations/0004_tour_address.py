# Generated by Django 2.2.3 on 2020-02-03 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20200203_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
    ]
