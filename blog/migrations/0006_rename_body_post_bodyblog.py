# Generated by Django 3.2.9 on 2021-11-13 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_image_post_upfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='bodyBlog',
        ),
    ]