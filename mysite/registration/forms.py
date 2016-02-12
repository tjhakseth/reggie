from django import forms
from .models import BuildUserInformation, Company

class UserInfoForm(forms.ModelForm):

    class Meta:
        model = BuildUserInformation
        fields = ('first_name', 'last_name')

# class CompanyForm(forms.ModelForm):

#     class Meta:
#         model = Company
#         exclude = ['password']