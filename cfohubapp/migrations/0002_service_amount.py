# Generated by Django 2.2.4 on 2020-05-30 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfohubapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='amount',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
