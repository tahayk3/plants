from typing import Text
from . models import plantas
from django import forms
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class MacetaForm(forms.ModelForm):
    class Meta: 
        model = plantas
        fields= '__all__'



















