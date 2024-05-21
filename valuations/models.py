from django.db import models
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password (retype)", widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match.')
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        # Add additional logic to process or store other form data here
        return user

# Create your models here.
