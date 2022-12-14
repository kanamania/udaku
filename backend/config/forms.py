from django.forms import forms, ModelForm, TextInput, ModelChoiceField, Select, ChoiceField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Region, Category, District, Setting, Log


class SelectWOA(Select):
    def create_option(self, name, value, label, selected, index,
                      subindex=None, attrs=None):
        option_dict = super(SelectWOA, self).create_option(name, value,
                                                           label, selected, index, subindex=subindex, attrs=attrs)
        # Category.objects.
        try:
            option_dict['attrs']['style'] = 'color: ' + Category.objects.get(name=label).color + ';'
        except:
            pass

        return option_dict


class CustomUserCreationForm(UserCreationForm):
    MY_CHOICES = [(None, 'Active'), (1, 'Inactive')]
    status = ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = None if self.instance.deleted_at is None else 1
        self.fields['status'].required = False

    class Meta:
        model = CustomUser
        fields = ("first_name", "middle_name", "last_name", "phone", "username", "email", "birthdate", "status")


class CustomUserChangeForm(UserChangeForm):
    MY_CHOICES = [(None, 'Active'), (1, 'Inactive')]
    status = ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = None if self.instance.deleted_at is None else 1
        self.fields['status'].required = False

    class Meta:
        model = CustomUser
        fields = ("first_name", "middle_name", "last_name", "phone", "username", "email", "birthdate", "status")


class CategoryCreationForm(ModelForm):
    MY_CHOICES = [(None, 'Active'), (1, 'Inactive')]
    status = ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(CategoryCreationForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = None if self.instance.deleted_at is None else 1
        self.fields['status'].required = False

    class Meta:
        model = Category
        fields = ("name", "description", "status")


class CategoryChangeForm(ModelForm):
    MY_CHOICES = [(None, 'Active'), (1, 'Inactive')]
    status = ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(CategoryChangeForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = None if self.instance.deleted_at is None else 1
        self.fields['status'].required = False

    class Meta:
        model = Category
        fields = ("name", "description", "status")


class RegionCreationForm(ModelForm):
    MY_CHOICES = [(None, 'Active'), (1, 'Inactive')]
    status = ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(RegionCreationForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = None if self.instance.deleted_at is None else 1
        self.fields['status'].required = False

    class Meta:
        model = Region
        fields = ("name", "status")


class RegionChangeForm(ModelForm):
    MY_CHOICES = [(None, 'Active'), (1, 'Inactive')]
    status = ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(RegionChangeForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = None if self.instance.deleted_at is None else 1
        self.fields['status'].required = False

    class Meta:
        model = Region
        fields = ("name", "status")


class DistrictCreationForm(ModelForm):
    MY_CHOICES = [(None, 'Active'), (1, 'Inactive')]
    status = ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(DistrictCreationForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = None if self.instance.deleted_at is None else 1
        self.fields['status'].required = False

    class Meta:
        model = District
        fields = ("name", "region", "status")


class DistrictChangeForm(ModelForm):
    MY_CHOICES = [(None, 'Active'), (1, 'Inactive')]
    status = ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(DistrictChangeForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = None if self.instance.deleted_at is None else 1
        self.fields['status'].required = False

    class Meta:
        model = District
        fields = ("name", "region", "status")


class SettingCreationForm(ModelForm):
    MY_CHOICES = [(None, 'Active'), (1, 'Inactive')]
    status = ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(SettingCreationForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = None if self.instance.deleted_at is None else 1
        self.fields['status'].required = False

    class Meta:
        model = Setting
        fields = ("category", "tag", "current_value", "description", "status")


class SettingChangeForm(ModelForm):
    MY_CHOICES = [(None, 'Active'), (1, 'Inactive')]
    status = ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(SettingChangeForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = None if self.instance.deleted_at is None else 1
        self.fields['status'].required = False

    class Meta:
        model = Setting
        fields = ("category", "tag", "current_value", "description", "status")


class LogCreationForm(ModelForm):
    MY_CHOICES = [(None, 'Active'), (1, 'Inactive')]
    status = ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(LogCreationForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = None if self.instance.deleted_at is None else 1
        self.fields['status'].required = False

    class Meta:
        model = Log
        fields = ("old", "tag", "new", "description", "status")


class LogChangeForm(ModelForm):
    MY_CHOICES = [(None, 'Active'), (1, 'Inactive')]
    status = ChoiceField(choices=MY_CHOICES)

    def __init__(self, *args, **kwargs):
        super(LogChangeForm, self).__init__(*args, **kwargs)
        self.fields['status'].initial = None if self.instance.deleted_at is None else 1
        self.fields['status'].required = False

    class Meta:
        model = Log
        fields = ("old", "tag", "new", "description", "status")
