from django.db import models


class Todo(models.Model):
    title = models.CharField('Название задания', max_length=500)
    is_completed = models.BooleanField('Завершено', default=False)
    description = models.TextField('Описание', null=True, blank=True)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title
