from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RecordForm(forms.Form):
    name = forms.CharField(max_length=20, label='Имя')
    family = forms.CharField(max_length=30, label='Фамилия')
    otchestvo = forms.CharField(max_length=30, label='Отчество', required=False)
    street = forms.CharField(max_length=30, label='Улица', required=False)
    house = forms.CharField(max_length=10, label='Дом', required=False)
    korp = forms.CharField(max_length=10, label='Корпус', required=False)
    apartments = forms.IntegerField(label='Квартира', required=False)
    mob = forms.CharField(max_length=25, label='Телефон')


#class RecordModelForm(forms.ModelForm):
#    family_string = forms.CharField(max_length=30, label='Фамилия')
#
#    class Meta:
#        model = Record
#        fields = ['name', 'otchestvo', 'street', 'house', 'korp', 'apartments', 'mob']
#