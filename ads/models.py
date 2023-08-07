from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=55, verbose_name='Название')
    description = models.TextField(null=True,
                                   blank=True,
                                   verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    publish_data = models.DateTimeField(verbose_name='Дата объявления')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'