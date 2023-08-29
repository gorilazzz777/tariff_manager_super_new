from django.db import models


class PartnersType(models.Model):
    name = models.CharField('Название', max_length=20)
    code = models.IntegerField('Код типа партнера')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип партнера'
        verbose_name_plural = 'Типы партнеров'


class Partner(models.Model):
    name = models.CharField('Название', max_length=150, null=True, blank=True)
    token = models.CharField('Токен', max_length=50)
    type = models.ForeignKey(PartnersType, on_delete=models.CASCADE, verbose_name='Тип контрагента',
                             blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'