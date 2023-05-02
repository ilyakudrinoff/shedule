from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Purposes(models.Model):
    name = models.CharField('Имя задачи', max_length=200)
    description = models.TextField('Описание задачи', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    deadline = models.DateTimeField('Срок исполнения')
    date_complete = models.DateTimeField('Исполнено', blank=True, null=True)
    what_is_do = models.TextField('Что сделано', blank=True, null=True)

    class Meta:
        ordering = ('deadline',)
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.name}'
