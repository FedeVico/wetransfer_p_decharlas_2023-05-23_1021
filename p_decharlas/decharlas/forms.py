from django import forms
from .models import User


class Font_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('font_type', 'font_size')
