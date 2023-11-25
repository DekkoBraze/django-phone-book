from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError


class RecordForm(forms.Form):
    name = forms.CharField(max_length=20, label='Имя')
    family = forms.CharField(max_length=30, label='Фамилия')
    otchestvo = forms.CharField(max_length=30, label='Отчество', required=False)
    street = forms.CharField(max_length=30, label='Улица', required=False)
    house = forms.CharField(max_length=10, label='Дом', required=False)
    korp = forms.CharField(max_length=10, label='Корпус', required=False)
    apartments = forms.IntegerField(label='Квартира', required=False)
    mob = forms.CharField(max_length=25, label='Телефон')

    def clean(self):
        mob = self.cleaned_data['mob']
        if Mob.objects.filter(value=mob).exists():
            raise ValidationError("Этот телефон уже записан в системе.")
        return super().clean()





