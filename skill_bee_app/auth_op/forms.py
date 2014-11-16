from django import forms
from auth_op.models import StudentUser, ClientUser
from django.contrib.auth.models import User

class UserRegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
      model = User
      fields = ('first_name', 'last_name', 'username', 'email', 'password')

class StudentRegForm(forms.ModelForm):

   class Meta:
     model = StudentUser
     fields = ('major', 'grad_year', 'gpa', 'portfolio')

class ClientRegForm(forms.ModelForm):

    class Meta:
      model = ClientUser
      fields = ('organization', 'phone_number')

