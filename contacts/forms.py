from django import forms

from .models import Contacts, Relationship, PreMeeting, Facts


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('name', 'last_name', 'photo', 'status', 'krug', 'sector', 'ois', 'first_info',)
        labels = {'name': 'Имя', 'last_name': 'Фамилия', 'photo': 'Фото', 'status': 'Статус', 'krug': 'Круг',
                  'sector': 'Сектор', 'ois': 'ОИС', 'first_info': 'Первичная информация'}


class PremeetingForm(forms.ModelForm):
    class Meta:
        model = PreMeeting
        fields = ('name', 'problem', 'plan', 'result',)
        labels = {'name': 'Имя встречи', 'problem': 'Проблема', 'plan': 'План развития отношений',
                  'result': 'Результат встречи'}


class RelationshipForm(forms.ModelForm):
    class Meta:
        model = Relationship
        fields = ('povedenie', 'results',)
        labels = {'povedenie': 'Поведение', 'results': 'Результат'}


class FactsForm(forms.ModelForm):
    class Meta:
        model = Facts
        fields = ('fact',)
        labels = {'fact': 'Факт'}
