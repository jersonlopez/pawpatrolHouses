# Generated by Django 2.0.2 on 2018-05-31 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0004_auto_20180528_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='userId',
            field=models.CharField(default='userUnknown', max_length=200),
        ),
    ]
