from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    creator = models.BigIntegerField()
    modifier = models.BigIntegerField(null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Region(models.Model):
    name = models.CharField(max_length=200)
    creator = models.BigIntegerField()
    modifier = models.BigIntegerField(null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class District(models.Model):
    name = models.CharField(max_length=200)
    region = models.BigIntegerField()
    creator = models.BigIntegerField()
    modifier = models.BigIntegerField(null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class Log(models.Model):
    tag = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    old = models.TextField(null=True)
    new = models.TextField(null=True)
    record = models.BigIntegerField()
    creator = models.BigIntegerField()
    created_at = models.DateTimeField()


class Setting(models.Model):
    tag = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    default_value = models.TextField(null=True)
    current_value = models.TextField(null=True)
    category = models.CharField(max_length=32)
    creator = models.BigIntegerField()
    modifier = models.BigIntegerField(null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True)


