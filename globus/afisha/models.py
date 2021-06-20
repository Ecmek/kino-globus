from django.db import models

from tinymce import models as tinymce_models

class ShowTime(models.Model):
    datetime = models.DateTimeField(
        verbose_name='���� ������',
    )
    price = models.PositiveIntegerField(
        verbose_name='���� ������',
    )
    format = models.CharField(
        verbose_name='������ ������',
    )

    class Meta:
        ordering = ['datetime']
        verbose_name = '����� ������'
        verbose_name_plural = '����� ������'

# TODO �������� ������ � ������
class Cinema(models.Model):
    title = models.CharField(
        max_length=50, null=False,
        verbose_name='�������� �����',
    )
    genre = models.CharField(
        max_length=20,
        verbose_name='���� �����'
    )
    trailer = tinymce_models.HTMLField(
        verbose_name='������� �������� <iframe>',
    )
    description = models.TextField(
        verbose_name='�������� �����',
    )
    mpaa = models.CharField(
        verbose_name='���������� �����������',
    )
    show_date = models.ManyToManyField(
        ShowTime,
        verbose_name='����� ������ �����',
    )

    class Meta:
        verbose_name = '�����'
        verbose_name_plural = '�����'

    def __str__(self):
        return self.title