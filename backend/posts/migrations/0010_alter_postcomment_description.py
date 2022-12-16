# Generated by Django 4.1.3 on 2022-12-15 08:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_postcomment_description_alter_postcomment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='description',
            field=models.TextField(null=True, validators=[django.core.validators.MinLengthValidator(12, 'comment description must contain at least 12 characters')]),
        ),
    ]