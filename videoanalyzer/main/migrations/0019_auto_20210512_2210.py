# Generated by Django 3.1.7 on 2021-05-12 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_facedetectionmodel_face_scale_factor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facedetectionmodel',
            name='face_scale_factor',
            field=models.FloatField(default=1.05, help_text='Help text', verbose_name='Face Scale Factor'),
        ),
    ]
