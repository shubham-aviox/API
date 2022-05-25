# Generated by Django 4.0.3 on 2022-04-07 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rel_app', '0002_remove_album_name_album_album_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='album_name',
        ),
        migrations.AddField(
            model_name='album',
            name='name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='track',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
