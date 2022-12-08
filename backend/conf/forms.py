from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("first_name", "middle_name", "last_name", "phone", "username", "email", "birthdate")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("first_name", "middle_name", "last_name", "phone", "username", "email", "birthdate")
