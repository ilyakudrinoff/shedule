# Generated by Django 4.1.4 on 2023-05-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purposes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purposes',
            name='what_is_do',
            field=models.TextField(blank=True, null=True, verbose_name='Что сделано'),
        ),
    ]