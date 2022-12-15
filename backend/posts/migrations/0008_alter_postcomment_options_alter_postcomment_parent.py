# Generated by Django 4.1.3 on 2022-12-15 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_remover_alter_postcomment_remover_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postcomment',
            options={'verbose_name': 'Post Comment', 'verbose_name_plural': 'Post Comments'},
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='posts.postcomment'),
        ),
    ]