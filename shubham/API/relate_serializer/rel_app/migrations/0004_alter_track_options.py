# Generated by Django 4.0.3 on 2022-04-07 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rel_app', '0003_remove_album_album_name_album_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['order']},
        ),
    ]
