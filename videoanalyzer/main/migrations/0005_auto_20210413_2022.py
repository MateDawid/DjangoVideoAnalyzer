# Generated by Django 3.1.7 on 2021-04-13 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210413_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circledetectionmodel',
            name='maxRadius',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='circledetectionmodel',
            name='minRadius',
            field=models.IntegerField(default=20),
        ),
    ]