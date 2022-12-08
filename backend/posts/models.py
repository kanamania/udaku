import hashlib

from django.contrib.auth.models import User
from django.db import models

from conf.models import CustomUser


def user_directory_path(instance, filename):
    return 'uploads/posts/user_{0}/{1}'.format(instance.user.id, hashlib.md5(filename.encode()).hexdigest())


class PostCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    category = models.BigIntegerField(null=True)
    creator = models.ForeignKey(CustomUser, related_name='created_post_categories', on_delete=models.DO_NOTHING)
    modifier = models.ForeignKey(CustomUser, related_name='modified_post_categories', blank=True, on_delete=models.DO_NOTHING)
    remover = models.ForeignKey(CustomUser, related_name='removed_post_categories', blank=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'post_category'


class Post(models.Model):
    image = models.ImageField(upload_to=user_directory_path)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    category = models.BigIntegerField(null=True)
    creator = models.ForeignKey(CustomUser, related_name='created_posts', on_delete=models.DO_NOTHING)
    modifier = models.ForeignKey(CustomUser, related_name='modified_posts', blank=True, on_delete=models.DO_NOTHING)
    remover = models.ForeignKey(CustomUser, blank=True, related_name='removed_posts', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'post'


class PostComment(models.Model):
    post = models.BigIntegerField()
    parent = models.BigIntegerField(null=True)
    description = models.TextField(null=True)
    creator = models.ForeignKey(CustomUser, related_name='created_post_comments', on_delete=models.DO_NOTHING)
    remover = models.ForeignKey(CustomUser, related_name='removed_post_comments', blank=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'post_comment'


class PostCommentReaction(models.Model):
    comment = models.BigIntegerField()
    reaction = models.IntegerField(default=1)
    creator = models.ForeignKey(CustomUser, related_name='created_post_comment_reactions', on_delete=models.DO_NOTHING)
    remover = models.ForeignKey(CustomUser, related_name='removed_post_comment_reactions', blank=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'post_comment_reaction'


class PostReaction(models.Model):
    post = models.BigIntegerField()
    reaction = models.IntegerField(default=1)
    creator = models.ForeignKey(CustomUser, related_name='created_post_reactions', on_delete=models.DO_NOTHING)
    remover = models.ForeignKey(CustomUser, related_name='removed_post_reactions', blank=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'post_reaction'

