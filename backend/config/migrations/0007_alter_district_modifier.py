# Generated by Django 4.1.3 on 2022-12-15 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0006_remove_category_parent_category_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='modifier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified_districts', to=settings.AUTH_USER_MODEL),
        ),
    ]
