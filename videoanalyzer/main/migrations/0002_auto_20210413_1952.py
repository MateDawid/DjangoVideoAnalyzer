# Generated by Django 3.1.7 on 2021-04-13 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CircleDetectionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', models.FloatField()),
                ('minDist', models.FloatField()),
                ('param1', models.FloatField()),
                ('param2', models.FloatField()),
                ('minRadius', models.FloatField()),
                ('maxRadius', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='DisplayModel',
        ),
    ]
