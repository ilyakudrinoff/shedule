from django import forms

from .models import Purposes


class PurposesForm(forms.ModelForm):
    class Meta:
        model = Purposes
        fields = ('name', 'description', 'deadline',)
        labels = {'name': 'Задача', 'description': 'Описание', 'Deadline': 'Дедлайн', }
        widgets = {'deadline': forms.DateInput(attrs={'type': 'datetime-local'})}
