# Generated by Django 3.1.4 on 2021-01-04 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0012_auto_20201227_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='room_photos'),
        ),
        migrations.AlterField(
            model_name='room',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='rooms.Tag'),
        ),
    ]