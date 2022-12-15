from django.db.models import Q
from django.forms import ModelForm, ChoiceField

from .models import *


class PostCreationForm(ModelForm):
    MY_CHOICES = [(None, 'Active'), (1, 'Inactive')]
    status = ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(PostCreationForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = None if self.instance.deleted_at is None else 1
        self.fields['status'].required = False

    class Meta:
        model = Post
        fields = ("name", "body", "description", "category", "status")


class PostChangeForm(ModelForm):
    MY_CHOICES = [(None, 'Active'), (1, 'Inactive')]
    status = ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(PostChangeForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = None if self.instance.deleted_at is None else 1
        self.fields['status'].required = False

    class Meta:
        model = Post
        fields = ("name", "body", "description", "category", "status")


class PostCategoryCreationForm(ModelForm):
    MY_CHOICES = [(None, 'Active'), (1, 'Inactive')]
    status = ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(PostCategoryCreationForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = None if self.instance.deleted_at is None else 1
        self.fields['status'].required = False

    class Meta:
        model = PostCategory
        fields = ("name", "description", "category", "status")


class PostCategoryChangeForm(ModelForm):
    MY_CHOICES = [(None, 'Active'), (1, 'Inactive')]
    status = ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(PostCategoryChangeForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = None if self.instance.deleted_at is None else 1
        self.fields['status'].required = False

    class Meta:
        model = PostCategory
        fields = ("name", "description", "category", "status")


class PostCommentCreationForm(ModelForm):
    MY_CHOICES = [(None, 'Active'), (1, 'Inactive')]
    status = ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(PostCommentCreationForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = None if self.instance.deleted_at is None else 1
        self.fields['status'].required = False
        self.fields['parent'].required = False

    class Meta:
        model = PostComment
        fields = ("post", "description", "parent", "status")


class PostCommentChangeForm(ModelForm):
    MY_CHOICES = [(None, 'Active'), (1, 'Inactive')]
    status = ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(PostCommentChangeForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = None if self.instance.deleted_at is None else 1
        self.fields['status'].required = False
        self.fields['parent'].required = False

    class Meta:
        model = PostComment
        fields = ("post", "description", "parent", "status")
