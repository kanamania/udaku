from rest_framework import serializers

from posts.models import *


class PostCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostCategory
        fields = ['id', 'name', 'description', 'creator', 'modifier', 'remover', 'created_at', 'updated_at',
                  'deleted_at']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'image', 'name', 'description', 'category', 'creator', 'modifier', 'remover', 'created_at', 'updated_at',
                  'deleted_at']


class PostReactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostReaction
        fields = ['id', 'post', 'reaction', 'creator', 'remover', 'created_at',
                  'deleted_at']


class PostCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostComment
        fields = ['id', 'post', 'parent', 'description', 'creator', 'remover', 'created_at', 'updated_at', 'deleted_at']


class PostCommentReactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostCommentReaction
        fields = ['id', 'comment', 'reaction', 'creator', 'remover', 'created_at', 'updated_at', 'deleted_at']
