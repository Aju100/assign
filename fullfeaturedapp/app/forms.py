from django import forms
from django.contrib.auth import get_user_model
from .models import Profile
#from django.forms.utils import ErrorList
from django.contrib.auth.forms import UserCreationForm

USER = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=200,widget=forms.PasswordInput())

class SignupForm(UserCreationForm):

    class Meta:
        model = USER
        fields =['first_name','last_name','username','email']

class UpdateForm(forms.Form):
  #  profile_image = forms.ImageField(upload_to='media')
    first_name = forms.CharField(max_length=15,required=True)
    last_name = forms.CharField(max_length=30,required=True)
    password = forms.CharField(max_length=200,required=True)