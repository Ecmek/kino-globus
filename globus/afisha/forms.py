from django import forms

from .models import Cinema, ShowTime


class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = '__all__'


class ShowTimeForm(forms.ModelForm):
    class Meta:
        model = ShowTime
        fields = '__all__'
