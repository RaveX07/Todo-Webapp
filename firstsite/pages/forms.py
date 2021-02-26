from django import forms

from .models import User
from .models import Todo

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'Name',
            'EMail',
            'Password'
        ]


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [
            'Name',
            'Content',
        ]
        
