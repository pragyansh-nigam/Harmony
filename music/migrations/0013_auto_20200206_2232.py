# Generated by Django 2.2.3 on 2020-02-06 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0012_playlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='muser',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/songtype/'),
        ),
        migrations.AddField(
            model_name='songgenre',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/songgenre/'),
        ),
    ]
