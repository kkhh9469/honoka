# Generated by Django 3.1.4 on 2020-12-21 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20201221_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='tag',
            field=models.ManyToManyField(blank=True, to='rooms.Tag'),
        ),
    ]
