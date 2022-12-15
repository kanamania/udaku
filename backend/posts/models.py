import hashlib

from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from ckeditor.fields import RichTextField

from config.models import CustomUser


def user_directory_path(instance, filename):
    return 'uploads/posts/user_{0}/{1}'.format(instance.user.id, hashlib.md5(filename.encode()).hexdigest())


class PostCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    category = models.ForeignKey('self', related_name='categories', blank=True, null=True, on_delete=models.SET_NULL)
    creator = models.ForeignKey(CustomUser, related_name='created_post_categories', on_delete=models.DO_NOTHING)
    modifier = models.ForeignKey(CustomUser, related_name='modified_post_categories', blank=True, null=True, on_delete=models.DO_NOTHING)
    remover = models.ForeignKey(CustomUser, related_name='removed_post_categories', blank=True, null=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'post_category'
        verbose_name = 'Post Category'
        verbose_name_plural = 'Post Categories'


class Post(models.Model):
    image = models.ImageField(upload_to=user_directory_path)
    name = models.CharField(max_length=200)
    body = RichTextField(null=True, validators=[
        MinLengthValidator(320, 'body must contain at least 320 characters')
    ])
    description = models.TextField(null=True, validators=[
        MaxLengthValidator(320, 'description must contain at most 320 characters')
    ])
    category = models.ForeignKey(PostCategory, related_name='posts', null=True, on_delete=models.SET_NULL)
    creator = models.ForeignKey(CustomUser, related_name='created_posts', on_delete=models.DO_NOTHING)
    modifier = models.ForeignKey(CustomUser, related_name='modified_posts', blank=True, null=True, on_delete=models.DO_NOTHING)
    remover = models.ForeignKey(CustomUser, blank=True, null=True, related_name='removed_posts', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'post'


class PostComment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.DO_NOTHING)
    parent = models.ForeignKey('self', related_name='comments', null=True, on_delete=models.DO_NOTHING)
    description = models.TextField(validators=[
        MinLengthValidator(12, 'comment description must contain at least 12 characters')
    ], null=True)
    creator = models.ForeignKey(CustomUser, related_name='created_post_comments', on_delete=models.DO_NOTHING)
    remover = models.ForeignKey(CustomUser, related_name='removed_post_comments', blank=True, null=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{} > {}".format(self.post, self.description)

    class Meta:
        db_table = 'post_comment'
        verbose_name = 'Post Comment'
        verbose_name_plural = 'Post Comments'


class PostCommentReaction(models.Model):
    comment = models.BigIntegerField()
    reaction = models.IntegerField(default=1)
    creator = models.ForeignKey(CustomUser, related_name='created_post_comment_reactions', on_delete=models.DO_NOTHING)
    remover = models.ForeignKey(CustomUser, related_name='removed_post_comment_reactions', blank=True, null=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'post_comment_reaction'


class PostReaction(models.Model):
    post = models.BigIntegerField()
    reaction = models.IntegerField(default=1)
    creator = models.ForeignKey(CustomUser, related_name='created_post_reactions', on_delete=models.DO_NOTHING)
    remover = models.ForeignKey(CustomUser, related_name='removed_post_reactions', blank=True, null=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'post_reaction'

