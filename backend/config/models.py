from django.contrib.auth.models import User, AbstractUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    middle_name = models.CharField(max_length=200, null=True)
    birthdate = models.DateField(null=True)
    phone = models.BigIntegerField(null=True)
    creator = models.BigIntegerField(default=1)
    modifier = models.BigIntegerField(null=True)
    remover = models.BigIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def status(self):
        return None if self.deleted_at is None else 1

    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    category = models.ForeignKey('self', related_name='categories', on_delete=models.SET_NULL, null=True)
    creator = models.ForeignKey(CustomUser, related_name='created_categories', on_delete=models.DO_NOTHING)
    modifier = models.ForeignKey(CustomUser, related_name='modified_categories', null=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def status(self):
        return None if self.deleted_at is None else 1

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=200)
    creator = models.ForeignKey(CustomUser, related_name='created_regions', on_delete=models.DO_NOTHING)
    modifier = models.ForeignKey(CustomUser, null=True, related_name='modified_regions', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'region'

    def status(self):
        return None if self.deleted_at is None else 1

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=200)
    region = models.ForeignKey(Region, related_name='districts', on_delete=models.DO_NOTHING)
    creator = models.ForeignKey(CustomUser, related_name='created_districts', on_delete=models.DO_NOTHING)
    modifier = models.ForeignKey(CustomUser, related_name='modified_districts', blank=True, null=True,
                                 on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'district'

    def status(self):
        return None if self.deleted_at is None else 1

    def __str__(self):
        return '{}: {}'.format(self.name, self.region.name)


class Log(models.Model):
    tag = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    old = models.TextField(null=True)
    new = models.TextField(null=True)
    record_type = models.CharField(max_length=128, null=True)
    record_id = models.BigIntegerField(null=True)
    creator = models.ForeignKey(CustomUser, related_name='created_log', null=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'log'

    def status(self):
        return None if self.deleted_at is None else 1

    def __str__(self):
        return '{}: {}'.format(self.tag, self.description)


class Setting(models.Model):
    tag = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    default_value = models.TextField(null=True)
    current_value = models.TextField(null=True)
    category = models.CharField(max_length=32)
    creator = models.ForeignKey(CustomUser, related_name='created_settings', on_delete=models.DO_NOTHING)
    modifier = models.ForeignKey(CustomUser, related_name='modified_settings', null=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'setting'

    def status(self):
        return None if self.deleted_at is None else 1

    def __str__(self):
        return '{}: {}'.format(self.tag, self.description)
