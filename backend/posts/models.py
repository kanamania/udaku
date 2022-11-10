import hashlib
from django.db import models


def user_directory_path(instance, filename):
    return 'uploads/posts/user_{0}/{1}'.format(instance.user.id, hashlib.md5(filename.encode()).hexdigest())


class PostCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    category = models.BigIntegerField(null=True)
    creator = models.BigIntegerField()
    modifier = models.BigIntegerField(null=True)
    remover = models.BigIntegerField(null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)


class Post(models.Model):
    image = models.ImageField(upload_to=user_directory_path)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    category = models.BigIntegerField(null=True)
    creator = models.BigIntegerField()
    remover = models.BigIntegerField(null=True)
    modifier = models.BigIntegerField(null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)


class PostComment(models.Model):
    post = models.BigIntegerField()
    parent = models.BigIntegerField(null=True)
    description = models.TextField(null=True)
    creator = models.BigIntegerField()
    remover = models.BigIntegerField(null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)


class PostCommentReaction(models.Model):
    comment = models.BigIntegerField()
    reaction = models.IntegerField(default=1)
    creator = models.BigIntegerField()
    remover = models.BigIntegerField(null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)


class PostReaction(models.Model):
    post = models.BigIntegerField()
    reaction = models.IntegerField(default=1)
    creator = models.BigIntegerField()
    remover = models.BigIntegerField(null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
