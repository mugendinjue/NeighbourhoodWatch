from django.contrib.auth.models import User
from .models import Security,Health,Profile,Business,Neighbourhood,Admin,Occupant,Posts
from django import forms
from django.contrib.auth.forms import UserCreationForm



class RegistrationForm(UserCreationForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email','password1','password2']


class NeighbourhoodCreationForm(forms.ModelForm):
  class Meta:
    model = Neighbourhood
    exclude = ['neighbourhood_admin','occupants','hood_logo']

class BusinessCreationForm(forms.ModelForm):
  class Meta:
    model = Business
    exclude = ['owner','neighbourhood']

class OccupantForm(forms.ModelForm):
  class Meta:
    model = Occupant
    exclude = ['user','neighbourhood']


class HealthContactsForm(forms.ModelForm):
  class Meta:
    model = Health
    exclude = ['neighbourhood']


class SecurityContactsForm(forms.ModelForm):
  class Meta:
    model = Security
    exclude = ['neighbourhood']


class UserPostForm(forms.ModelForm):
  class Meta:
    model = Posts
    exclude = ['user','neighbourhood']
    


