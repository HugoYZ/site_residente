# Generated by Django 3.0.2 on 2020-02-14 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco_proyectos', '0008_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='pdf',
        ),
        migrations.AddField(
            model_name='media',
            name='save',
            field=models.ImageField(default=None, upload_to='media/% Y/% m/% d/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='upload',
            field=models.ImageField(default=None, upload_to='media/'),
            preserve_default=False,
        ),
    ]
