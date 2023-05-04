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
        fields = ('commitment_intensity', 'initiative_reciprocity', 'emotional_involment', 'openness_trust')
        labels = {'commitment_intensity': 'Приверженность и интенсивность',
                  'initiative_reciprocity': 'Инициатива и взаимность',
                  'emotional_involment': 'Эмоциональная вовлеченность',  'openness_trust': 'Открытость и доверие', }


class FactsForm(forms.ModelForm):
    class Meta:
        model = Facts
        fields = ('fact',)
        labels = {'fact': 'Факт'}
