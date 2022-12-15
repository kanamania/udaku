# Generated by Django 4.1.3 on 2022-12-15 06:58

import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_alter_postcategory_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(null=True, validators=[django.core.validators.MinLengthValidator(320, 'body must contain at least 320 characters')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.postcategory'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(null=True, validators=[django.core.validators.MaxLengthValidator(320, 'description must contain at most 320 characters')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='modifier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]