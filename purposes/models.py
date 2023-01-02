from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Purposes(models.Model):
    name = models.CharField('Цель', max_length=200)
    description = models.TextField('Описание цели', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    deadline = models.DateTimeField('Дедлайн')
    date_complete = models.DateTimeField('Дата комплита', blank=True, null=True)

    class Meta:
        ordering = ('deadline',)
        verbose_name = 'Список целей'
        verbose_name_plural = 'Список целей'

    def __str__(self):
        return f'{self.name}'


class Tasks(models.Model):
    name = models.CharField('Задача', max_length=200)
    description = models.TextField('Описание задачи', blank=True, null=True)
    deadline = models.DateTimeField('Дедлайн')
    date_complete = models.DateTimeField('Дата комплита', blank=True, null=True)
    purpose = models.ForeignKey(Purposes, on_delete=models.CASCADE, verbose_name='Цель')

    class Meta:
        ordering = ('deadline',)
        verbose_name = 'Список задач'
        verbose_name_plural = 'Список задач'

    def __str__(self):
        return f'{self.name}'
