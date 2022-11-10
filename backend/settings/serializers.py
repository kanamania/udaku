from django.contrib.auth.models import User
from rest_framework import serializers
from settings.models import District, Region, Category, Log, Setting


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'first_name', 'last_name', 'username', 'email', 'groups']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'description', 'name', 'creator', 'modifier', 'created_at', 'updated_at']


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'creator', 'modifier', 'created_at', 'updated_at']


class DistrictSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'region', 'name', 'creator', 'modifier', 'created_at', 'updated_at']


class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log
        fields = ['id', 'tag', 'description', 'old', 'new', 'record' 'creator', 'created_at']


class SettingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Setting
        fields = ['id', 'tag', 'description', 'default_value', 'current_value', 'category' 'creator', 'modifier',
                  'created_at', 'updated_at']
