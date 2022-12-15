from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return "{} {}".format(obj.first_name, obj.last_name)

    class Meta:
        model = CustomUser
        read_only_fields = ('creator', 'modifier', 'remover', 'created_at', 'updated_at', 'deleted_at')
        fields = ['id', 'url', 'name', 'first_name', 'last_name', 'username', 'email', 'groups']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
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
        model = Category
        read_only_fields = ('creator', 'modifier', 'remover', 'created_at', 'updated_at', 'deleted_at')
        fields = ['id', 'description', 'name', 'creator', 'creator_name', 'modifier', 'modifier_name', 'created_at',
                  'updated_at']


class RegionSerializer(serializers.HyperlinkedModelSerializer):
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
        model = Region
        read_only_fields = ('creator', 'modifier', 'remover', 'created_at', 'updated_at', 'deleted_at')
        fields = ['id', 'name', 'creator', 'creator_name', 'modifier', 'modifier_name', 'created_at', 'updated_at']


class DistrictSerializer(serializers.HyperlinkedModelSerializer):
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
        model = District
        read_only_fields = ('creator', 'modifier', 'remover', 'created_at', 'updated_at', 'deleted_at')
        fields = ['id', 'region', 'name', 'creator', 'creator_name', 'modifier', 'modifier_name', 'created_at',
                  'updated_at']


class LogSerializer(serializers.HyperlinkedModelSerializer):
    creator_name = serializers.SerializerMethodField()

    def get_creator_name(self, obj):
        return obj.creator.username

    class Meta:
        model = Log
        read_only_fields = ('creator', 'modifier', 'remover', 'created_at', 'updated_at', 'deleted_at')
        fields = ['id', 'tag', 'description', 'old', 'new', 'record_type', 'record_id', 'creator', 'creator_name', 'created_at']


class SettingSerializer(serializers.HyperlinkedModelSerializer):
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
        model = Setting
        read_only_fields = ('creator', 'modifier', 'remover', 'created_at', 'updated_at', 'deleted_at')
        fields = ['id', 'tag', 'description', 'default_value', 'current_value', 'category', 'creator', 'creator_name',
                  'modifier', 'modifier_name',
                  'created_at', 'updated_at']
