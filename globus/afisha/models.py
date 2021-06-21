from django.utils import timezone
from django.db import models


# TODO добавить постер к фильму
class Cinema(models.Model):
    title = models.CharField(max_length=50, null=False, verbose_name='Название ленты',)
    genre = models.CharField(max_length=50, verbose_name='Жанр ленты')
    duration = models.CharField(max_length=50, verbose_name='Длительность ленты')
    trailer = models.TextField(verbose_name='Вставка трейлера <iframe>',)
    description = models.TextField(verbose_name='Описание ленты',)
    mpaa = models.CharField(max_length=10, verbose_name='Возрастные ограничения',)
    source = models.CharField(max_length=200, verbose_name='Ссылка на источник')

    class Meta:
        verbose_name = 'Лента'
        verbose_name_plural = 'Ленты'

    def __str__(self):
        return self.title


class ShowTime(models.Model):
    datetime = models.DateTimeField(verbose_name='Дата показа',)
    price = models.PositiveIntegerField(verbose_name='Цена билета',)
    format = models.CharField(max_length=10, verbose_name='Формат ленты',)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name='Лента', related_name='show_time')

    class Meta:
        ordering = ['datetime']
        verbose_name = 'Время показа'
        verbose_name_plural = 'Время показа'

    def recentle_show(self):
        return self.datetime >= timezone.now()
