from django.contrib.auth.models import User
from rest_framework import serializers

from config.serializers import UserSerializer
from .models import *
from config.models import CustomUser


class PostCategorySerializer(serializers.HyperlinkedModelSerializer):
    creator_name = serializers.SerializerMethodField()
    modifier_name = serializers.SerializerMethodField()

    def get_creator_name(self, obj):
        return obj.creator.username

    def get_modifier_name(self, obj):
        try:
            return obj.modifier.username
        except:
            return ''

    class Meta:
        model = PostCategory
        fields = ['id', 'name', 'description', 'creator', 'creator_name', 'modifier', 'modifier_name', 'remover', 'created_at', 'updated_at',
                  'deleted_at']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    creator_name = serializers.SerializerMethodField()
    modifier_name = serializers.SerializerMethodField()

    def get_creator_name(self, obj):
        return obj.creator.username

    def get_modifier_name(self, obj):
        try:
            return obj.modifier.username
        except:
            return ''

    class Meta:
        model = Post
        fields = ['id', 'image', 'name', 'description', 'category', 'creator', 'creator_name', 'modifier', 'modifier_name', 'remover', 'created_at', 'updated_at',
                  'deleted_at']


class PostReactionSerializer(serializers.HyperlinkedModelSerializer):
    creator_name = serializers.SerializerMethodField()
    modifier_name = serializers.SerializerMethodField()

    def get_creator_name(self, obj):
        return obj.creator.username

    def get_modifier_name(self, obj):
        try:
            return obj.modifier.username
        except:
            return ''

    class Meta:
        model = PostReaction
        fields = ['id', 'post', 'reaction', 'creator', 'creator_name', 'remover', 'created_at',
                  'deleted_at']


class PostCommentSerializer(serializers.HyperlinkedModelSerializer):
    creator_name = serializers.SerializerMethodField()
    modifier_name = serializers.SerializerMethodField()

    def get_creator_name(self, obj):
        return obj.creator.username

    def get_modifier_name(self, obj):
        try:
            return obj.modifier.username
        except:
            return ''

    class Meta:
        model = PostComment
        fields = ['id', 'post', 'parent', 'description', 'creator', 'creator_name', 'remover', 'created_at', 'updated_at', 'deleted_at']


class PostCommentReactionSerializer(serializers.HyperlinkedModelSerializer):
    creator_name = serializers.SerializerMethodField()
    modifier_name = serializers.SerializerMethodField()

    def get_creator_name(self, obj):
        return obj.creator.username

    def get_modifier_name(self, obj):
        try:
            return obj.modifier.username
        except:
            return ''

    class Meta:
        model = PostCommentReaction
        fields = ['id', 'comment', 'reaction', 'creator', 'creator_name', 'remover', 'created_at', 'updated_at', 'deleted_at']
