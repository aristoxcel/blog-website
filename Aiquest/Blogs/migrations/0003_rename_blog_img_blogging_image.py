# Generated by Django 4.2.5 on 2023-09-24 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0002_alter_blogging_blog_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogging',
            old_name='blog_img',
            new_name='image',
        ),
    ]
