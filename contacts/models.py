from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


STATUS = (
    ('Коннектор', 'Коннектор'),
    ('Конденсатор', 'Конденсатор'),
    ('Проводник', 'Проводник'),
    ('Привратник', 'Привратник'),
)

KRUG = (
    ('Круг поддержки', 'Круг поддержки'),
    ('Круг продуктивности', 'Круг продуктивности'),
    ('Круг развития', 'Круг развития'),
)

OIS = (
    ('Опасен', 'Опасен'),
    ('Интересен', 'Интересен'),
    ('Сложен', 'Сложен'),
)

MARKS = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)


class Sectors(TimeStampedModel):
    name = models.CharField('Сектор', max_length=50)

    class Meta:
        ordering = ('name',)
        verbose_name = 'сектор'
        verbose_name_plural = 'секторы'

    def __str__(self):
        return f'{self.name}'


class Contacts(TimeStampedModel):
    name = models.CharField('Имя контакта', max_length=20)
    last_name = models.CharField('Фамилия контакта', max_length=20)
    photo = models.ImageField('Фото', blank=True, null=True, upload_to='images/')
    status = models.CharField('Статус', choices=STATUS, max_length=20)
    krug = models.CharField('Круг контактов', choices=KRUG, max_length=20)
    sector = models.ForeignKey(Sectors, on_delete=models.DO_NOTHING, related_name='sector', blank=True, null=True,
                               verbose_name='Сектор')
    ois = models.CharField('ОИС', choices=OIS, max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    first_info = models.TextField('Первичная информация', blank=True, null=True)

    class Meta:
        ordering = ('krug',)
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'

    def __str__(self):
        return f'{self.name}'


class PreMeeting(TimeStampedModel):
    name = models.CharField('Имя встречи', max_length=50)
    what_will_do = models.TextField('Что сделать для развития отношений')
    how_know_about = models.TextField('Как узнать больше о человеке')
    what_will_give = models.TextField('Что я могу дать')
    what_will_get = models.TextField('Что я могу попросить')
    how_next_meet = models.TextField('Как обеспечить следующую встречу')
    result = models.TextField('Результат встречи', blank=True, null=True)
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE, related_name='meet_contact', verbose_name='Контакт')

    class Meta:
        ordering = ('contact',)
        verbose_name = 'предвстреча'
        verbose_name_plural = 'предвстречи'

    def __str__(self):
        return f'{self.name}'


POVEDENIE = (
    ('приверженность и интенсивность', 'приверженность и интенсивность'),
    ('инициатива и взаимность', 'инициатива и взаимность'),
    ('эмоциональная вовлеченность', 'эмоциональная вовлеченность'),
    ('открытость и доверие', 'открытость и доверие'),
)


class Relationship(TimeStampedModel):
    commitment_intensity = models.CharField('Приверженность и интенсивность', choices=MARKS, max_length=2)
    initiative_reciprocity = models.CharField('Инициатива и взаимность', choices=MARKS, max_length=2)
    emotional_involment = models.CharField('Эмоциональная вовлеченность', choices=MARKS, max_length=2)
    openness_trust = models.CharField('Открытость и доверие', choices=MARKS, max_length=2)
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE, related_name='ship_contact', verbose_name='Контакт')

    class Meta:
        ordering = ('contact',)
        verbose_name = 'отношение'
        verbose_name_plural = 'отношения'

    def __str__(self):
        return f'{self.contact}'


class Facts(TimeStampedModel):
    fact = models.TextField('Факт')
    contact = models.ForeignKey(Contacts, on_delete=models.CASCADE, related_name='fact_contact', verbose_name='Контакт')

    class Meta:
        ordering = ('contact',)
        verbose_name = 'факт'
        verbose_name_plural = 'факты'

    def __str__(self):
        return f'{self.contact}'
