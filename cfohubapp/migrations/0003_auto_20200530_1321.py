# Generated by Django 2.2.4 on 2020-05-30 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfohubapp', '0002_service_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
