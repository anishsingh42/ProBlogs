# Generated by Django 4.2 on 2023-05-26 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_user_remove_category_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='cat_created_at',
            new_name='post_created_at',
        ),
    ]
