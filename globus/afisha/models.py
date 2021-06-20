from django.db import models

from tinymce import models as tinymce_models

class ShowTime(models.Model):
    datetime = models.DateTimeField(
        verbose_name='Дата показа',
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена билета',
    )
    format = models.CharField(
        verbose_name='Формат показа',
    )

    class Meta:
        ordering = ['datetime']
        verbose_name = 'Время показа'
        verbose_name_plural = 'Время показа'

# TODO добавить постер к фильму
class Cinema(models.Model):
    title = models.CharField(
        max_length=50, null=False,
        verbose_name='Название ленты',
    )
    genre = models.CharField(
        max_length=20,
        verbose_name='Жанр ленты'
    )
    trailer = tinymce_models.HTMLField(
        verbose_name='Вставка трейлера <iframe>',
    )
    description = models.TextField(
        verbose_name='Описание ленты',
    )
    mpaa = models.CharField(
        verbose_name='Возрастные ограничения',
    )
    show_date = models.ManyToManyField(
        ShowTime,
        verbose_name='время показа ленты',
    )

    class Meta:
        verbose_name = 'Лента'
        verbose_name_plural = 'Ленты'

    def __str__(self):
        return self.title