# Generated by Django 4.1.3 on 2022-12-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_category_deleted_at_district_deleted_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
