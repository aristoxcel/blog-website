# Generated by Django 4.2.5 on 2023-09-24 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogging',
            name='blog_img',
            field=models.ImageField(default='def.png', upload_to='pic/'),
        ),
    ]
