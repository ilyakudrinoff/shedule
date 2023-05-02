# Generated by Django 4.1.4 on 2023-05-02 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Purposes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя задачи')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание задачи')),
                ('deadline', models.DateTimeField(verbose_name='Срок исполнения')),
                ('date_complete', models.DateTimeField(blank=True, null=True, verbose_name='Исполнено')),
                ('what_is_do', models.TextField(verbose_name='Что сделано')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ('deadline',),
            },
        ),
    ]
