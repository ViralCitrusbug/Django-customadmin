# -*- coding: utf-8 -*-

from django import forms

# from ..forms import ServiceChangeForm

from django.contrib.auth.models import User


# -----------------------------------------------------------------------------
# User
# -----------------------------------------------------------------------------

class UserCreationForm(forms.ModelForm):
    """Custom User"""

    class Meta():
        model = User
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "username",
        ]

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        # print(cleaned_data)
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        last_name = cleaned_data.get("last_name")
        first_name = cleaned_data.get("first_name")

        if not email :
            raise forms.ValidationError(
                "Please add email."
            )
        if not password :
            raise forms.ValidationError(
                "Please add Password."
            )
        if not last_name :
            raise forms.ValidationError(
                "Please add last name."
            )
        if not first_name :
            raise forms.ValidationError(
                "Please add first name."
            )
    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class UserChangeForm(forms.ModelForm):
    """Custom form to change User"""

    class Meta():
        model = User

        fields = [
            "email",
           
            "first_name",
            "last_name",
            "username",
        ]

    def clean(self):
        print(type(self.instance))
        # cleaned_data = super(ServiceChangeForm, self.instance).clean()
        # email = cleaned_data.get("email")
        # password = cleaned_data.get("password")
        # last_name = cleaned_data.get("last_name")
        # first_name = cleaned_data.get("first_name")

        # if not email :
        #     raise forms.ValidationError(
        #         "Please add email."
        #     )
        # if not password :
        #     raise forms.ValidationError(
        #         "Please add Password."
        #     )
        # if not last_name :
        #     raise forms.ValidationError(
        #         "Please add last name."
        #     )
        # if not first_name :
        #     raise forms.ValidationError(
        #         "Please add first name."
        #     )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance