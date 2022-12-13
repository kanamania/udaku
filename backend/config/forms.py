from django.forms import forms, ModelForm, TextInput, ModelChoiceField, Select
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

    class Meta:
        model = CustomUser
        fields = ("first_name", "middle_name", "last_name", "phone", "username", "email", "birthdate")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("first_name", "middle_name", "last_name", "phone", "username", "email", "birthdate")


class CategoryCreationForm(ModelForm):

    class Meta:
        model = Category
        fields = ("name", "description")


class CategoryChangeForm(ModelForm):

    class Meta:
        model = Category
        fields = ("name", "description")


class RegionCreationForm(ModelForm):

    class Meta:
        model = Region
        fields = ("name",)


class RegionChangeForm(ModelForm):

    class Meta:
        model = Region
        fields = ("name",)


class DistrictCreationForm(ModelForm):

    class Meta:
        model = District
        fields = ("name", "region")


class DistrictChangeForm(ModelForm):

    class Meta:
        model = District
        fields = ("name", "region")


class SettingCreationForm(ModelForm):

    class Meta:
        model = Setting
        fields = ("category", "tag", "current_value", "description")


class SettingChangeForm(ModelForm):

    class Meta:
        model = Setting
        fields = ("category", "tag", "current_value", "description")


class LogCreationForm(ModelForm):

    class Meta:
        model = Log
        fields = ("old", "tag", "new", "description")


class LogChangeForm(ModelForm):

    class Meta:
        model = Log
        fields = ("old", "tag", "new", "description")
