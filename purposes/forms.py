from django import forms

from .models import Tasks, Purposes


class PurposesForm(forms.ModelForm):
    class Meta:
        model = Purposes
        fields = ('name', 'description', 'deadline',)
        labels = {'name': 'Цель', 'description': 'Описание', 'Deadline': 'Дедлайн', }


class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('name', 'description', 'deadline',)
        labels = {'name': 'Задача', 'description': 'Описание', 'Deadline': 'Дедлайн', }
