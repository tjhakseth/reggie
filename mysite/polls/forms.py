from django import forms
from .models import Build_User_Information

class UserInfoForm(forms.ModelForm):

    class Meta:
        model = Build_User_Information
        fields = ('first_name', 'last_name')