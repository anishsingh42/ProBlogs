# Generated by Django 4.2 on 2023-05-22 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_post_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='image_post',
        ),
    ]
