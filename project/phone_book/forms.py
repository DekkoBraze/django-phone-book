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

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk')
        super(RecordForm, self).__init__(*args, **kwargs)

    def clean(self):
        mob = self.cleaned_data['mob']
        mob_object = Mob.objects.filter(value=mob)
        try:
            if mob_object.exists() and mob_object[0].record.id != self.pk:
                raise ValidationError("Этот телефон уже записан в системе.")
        except Record.DoesNotExist:
            raise ValidationError("Этот телефон уже записан в системе.")
        return super().clean()
#Mob.objects.filter(value=mob).exclude(id=self.pk).values('id')


class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['value']
        labels = {
            'value': 'Фамилия',
        }


class NameForm(forms.ModelForm):
    class Meta:
        model = Name
        fields = ['value']
        labels = {
            'value': 'Имя',
        }


class OtchestvoForm(forms.ModelForm):
    class Meta:
        model = Otchestvo
        fields = ['value']
        labels = {
            'value': 'Отчество',
        }


class StreetForm(forms.ModelForm):
    class Meta:
        model = Street
        fields = ['value']
        labels = {
            'value': 'Улица',
        }


class MobForm(forms.ModelForm):
    class Meta:
        model = Mob
        fields = ['value']
        labels = {
            'value': 'Телефон',
        }