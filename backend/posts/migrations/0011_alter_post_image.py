# Generated by Django 4.1.3 on 2022-12-15 12:09

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_postcomment_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=posts.models.user_directory_path),
        ),
    ]