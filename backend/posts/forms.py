from django.forms import ModelForm, ChoiceField

from .models import Post


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
