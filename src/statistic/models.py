from django.db import models

from statistic.manager.statistic import StatisticClassManager


class Route(models.Model):
    sender = models.CharField('Код города отправителя', max_length=10)
    receiver = models.CharField('Код города получателя', max_length=10)

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'


class Package(models.Model):
    name = models.CharField('Название', max_length=35)
    code = models.CharField('Код', max_length=10)
    weight = models.FloatField('Вес')

    class Meta:
        verbose_name = 'Упаковка'
        verbose_name_plural = 'Упаковки'


class Statistic(models.Model):
    delivered = models.IntegerField('Доставлено', default=0)
    rejection = models.IntegerField('Отказ', default=0)
    amount = models.IntegerField('Сумма', default=0)
    date = models.DateField('Дата')
    partner = models.ForeignKey('partner.Partner', on_delete=models.CASCADE, related_name='statistic')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='statistic')
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='statistic')

    objects = models.Manager()
    manager = StatisticClassManager()

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистики'
        indexes = [
            models.Index(fields=['date']),
            models.Index(fields=['date', 'partner']),
            models.Index(fields=['date', 'route']),
            models.Index(fields=['date', 'package']),
            models.Index(fields=['date', 'partner', 'route']),
            models.Index(fields=['date', 'partner', 'package']),
            models.Index(fields=['date', 'route', 'package']),
            models.Index(fields=['date', 'partner', 'route', 'package']),
        ]
