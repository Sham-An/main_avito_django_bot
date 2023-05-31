from django.db import models

from .constants import STATUS_NEW, STATUS_READY
import datetime


# STATUS_NEW = 1
# STATUS_READY = 2


class Task(models.Model):
    title = models.TextField(
        verbose_name='Название задания',
        unique=True,
    )
    url = models.URLField(
        verbose_name='Ссылка на раздел',
        unique=True,
    )
    status = models.IntegerField(
        verbose_name='Статус задания',
        choices=(
            (STATUS_NEW, 'Новое'),
            (STATUS_READY, 'Готово'),
        ),
        default=STATUS_NEW,
    )

    def __str__(self):
        return f'#{self.pk} {self.title}'

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'


class Product(models.Model):
    task = models.ForeignKey(
        to=Task,
        verbose_name='Задание',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
    )
    title = models.CharField(verbose_name='Заголовок', max_length=500)  # CharField
    description = models.TextField(verbose_name='Объявление', blank=True)
    price = models.PositiveIntegerField(verbose_name='Цена')
    currency = models.TextField(verbose_name='Валюта', null=True, blank=True)
    # location = models.CharField(max_length=255)
    url = models.URLField(verbose_name='Ссылка на объявление', unique=True)
    #published_date = models.DateTimeField(default=datetime.date, verbose_name='Дата публикации', blank=True, null=True)
    published_date = models.DateTimeField(default=datetime.datetime.now(), verbose_name='Дата публикации', blank=True, null=True)
    # image_url = models.URLField()
    # date_upgrade = models.DateTimeField(default=datetime.date, verbose_name='Дата изменения', blank=True, null=True)
    seller_url = models.URLField(verbose_name='Продавец', blank=True, unique=False)

    def __str__(self):
        return f'#{self.pk} {self.title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class path_xpath(models.Model):
    path_name = models.TextField(
        verbose_name='Название поля',
        blank=True,
        unique=False,
    )
    path_str = models.TextField(
        verbose_name='XPATH',
        blank=True,
        unique=False,
    )


class Categories(models.Model):
    cat_id = models.IntegerField('kod_id')
    name = models.CharField(verbose_name='Категория', max_length=255, blank=True)
    parent_id = models.IntegerField('index', blank=True)
    url_path = models.CharField(max_length=255, blank=True)
    url_name = models.CharField(verbose_name='altername', max_length=255, blank=True)


class Region(models.Model):
    region_id = models.IntegerField('kod_id')
    kod_region = models.CharField('код авто', max_length=255, blank=True)
    name = models.CharField('Регион', max_length=255, blank=True)
    url_path = models.CharField(verbose_name='URL_path', max_length=255, blank=True)
    url_name = models.CharField(verbose_name='URL_name', max_length=255, blank=True)
    index_post = models.IntegerField(verbose_name='почтовый индекс', blank=True)

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return self.name


class City(models.Model):
    # avito_id = models.IntegerField('ID')
    city_id = models.IntegerField('kod_id')
    name = models.CharField(verbose_name='Нас пункт', max_length=255, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Регион')
    # region = models.IntegerField(verbose_name='Регион', blank=True) #models.ForeignKey(Region.region_id, on_delete=models.CASCADE, verbose_name='Регион')
    # parent_id = models.IntegerField(blank=True)
    url_path = models.CharField(verbose_name='URL_path', max_length=255, blank=True)
    url_name = models.CharField(verbose_name='altername', max_length=255, blank=True)
    index_post = models.IntegerField('index', blank=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name
