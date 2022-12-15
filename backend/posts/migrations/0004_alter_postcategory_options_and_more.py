# Generated by Django 4.1.3 on 2022-12-15 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_body_alter_post_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postcategory',
            options={'verbose_name': 'Post Category', 'verbose_name_plural': 'Post Categories'},
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='posts.postcategory'),
        ),
    ]
