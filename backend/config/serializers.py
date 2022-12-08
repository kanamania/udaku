from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'url', 'first_name', 'last_name', 'username', 'email', 'groups']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    creator_name = serializers.SerializerMethodField()
    modifier_name = serializers.SerializerMethodField()

    def get_creator_name(self, obj):
        return UserSerializer(obj.creator).name

    def get_modifier_name(self, obj):
        try:
            modifier = CustomUser.objects.filter(pk=obj.modifier).first()
            return modifier.first_name + ' ' + modifier.last_name
        except:
            return ''

    class Meta:
        model = Category
        fields = ['id', 'description', 'name', 'creator', 'creator_name', 'modifier', 'modifier_name', 'created_at',
                  'updated_at']


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    creator_name = serializers.SerializerMethodField()
    modifier_name = serializers.SerializerMethodField()

    def get_creator_name(self, obj):
        return UserSerializer(obj.creator).name

    def get_modifier_name(self, obj):
        try:
            modifier = CustomUser.objects.filter(pk=obj.modifier).first()
            return modifier.first_name + ' ' + modifier.last_name
        except:
            return ''

    class Meta:
        model = Region
        fields = ['id', 'name', 'creator', 'creator_name', 'modifier', 'modifier_name', 'created_at', 'updated_at']


class DistrictSerializer(serializers.HyperlinkedModelSerializer):
    creator_name = serializers.SerializerMethodField()
    modifier_name = serializers.SerializerMethodField()

    def get_creator_name(self, obj):
        return UserSerializer(obj.creator).name

    def get_modifier_name(self, obj):
        try:
            modifier = CustomUser.objects.filter(pk=obj.modifier).first()
            return modifier.first_name + ' ' + modifier.last_name
        except:
            return ''

    class Meta:
        model = District
        fields = ['id', 'region', 'name', 'creator', 'creator_name', 'modifier', 'modifier_name', 'created_at',
                  'updated_at']


class LogSerializer(serializers.HyperlinkedModelSerializer):
    creator_name = serializers.SerializerMethodField()
    modifier_name = serializers.SerializerMethodField()

    def get_creator_name(self, obj):
        return UserSerializer(obj.creator).name

    class Meta:
        model = Log
        fields = ['id', 'tag', 'description', 'old', 'new', 'record' 'creator', 'creator_name', 'created_at']


class SettingSerializer(serializers.HyperlinkedModelSerializer):
    creator_name = serializers.SerializerMethodField()
    modifier_name = serializers.SerializerMethodField()

    def get_creator_name(self, obj):
        return UserSerializer(obj.creator).name

    def get_modifier_name(self, obj):
        try:
            modifier = CustomUser.objects.filter(pk=obj.modifier).first()
            return modifier.first_name + ' ' + modifier.last_name
        except:
            return ''

    class Meta:
        model = Setting
        fields = ['id', 'tag', 'description', 'default_value', 'current_value', 'category' 'creator', 'creator_name',
                  'modifier', 'modifier_name',
                  'created_at', 'updated_at']
