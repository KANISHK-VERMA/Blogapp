from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
class Userregisterform(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','password1','password2','email']


class Userupdateform(forms.ModelForm):
    email= forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']


class Profileupdateform(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']