from django import forms

from .models import Tasks, Purposes


class PurposesForm(forms.ModelForm):
    class Meta:
        model = Purposes
        fields = ('name', 'description', 'deadline',)
        labels = {'name': 'Цель', 'description': 'Описание', 'Deadline': 'Дедлайн', }
        widgets = {'deadline': forms.DateInput(attrs={'type': 'datetime-local'})}


class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('name', 'description', 'deadline', 'purpose')
        labels = {'purpose': 'Цель', 'name': 'Задача', 'description': 'Описание', 'deadline': 'Дедлайн', }
        widgets = {'deadline': forms.DateInput(attrs={'type': 'datetime-local'})}
