from django import forms
from  myapp.models import UserModel
import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _



class UserForm(forms.Form):
    username=forms.EmailField(max_length=150,label="UserName/Email")
    password=forms.CharField(max_length=150,widget=forms.PasswordInput(),help_text="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters")
    confirm_password=forms.CharField(max_length=150,widget=forms.PasswordInput(),label="confirm password",help_text="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters")

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")



class ForgetForm(forms.Form):
    username=forms.EmailField(max_length=150)




