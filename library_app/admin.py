from django.contrib import admin
from . import models
from django import forms

class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ('first_name', 'last_name', 'birth_date', 'death_date', 'birth_place', 'death_place')
