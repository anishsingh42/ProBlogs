# Generated by Django 4.2 on 2023-05-26 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_alter_category_cat_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='cat_created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_created_at',
        ),
    ]