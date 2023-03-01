from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User


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
        fields = ['username','email']        