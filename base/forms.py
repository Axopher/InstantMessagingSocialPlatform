from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','email','password1','password2']

class RoomForm(ModelForm):
    class Meta:
        # room is the model that we wanna create form for
        model = Room
        # this will create form based on room inside models.py
        fields = '__all__' 
        exclude = ['host','participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username','email','bio']        