from datetime import datetime

from django.db import models


class Todo(models.Model):
    title = models.CharField('Название задания', max_length=500)
    is_completed = models.BooleanField('Завершено', default=False)
    description = models.TextField('Описание', null=True, blank=True)
    created_at = models.DateField('Дата добавления', default=datetime.now(), blank=True)
    deadline = models.DateField('Срок выполнения', blank=True, null=True)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title
