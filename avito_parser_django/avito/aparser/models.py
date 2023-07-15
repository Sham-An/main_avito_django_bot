from django.db import models
import sys
sys.path.insert(0, '/opt/opt2/PycharmProjects/main_avito_django_bot/avito_parser_django/avito/aparser')
#from .constants import STATUS_NEW, STATUS_READY
import datetime
#from avito.avito.settings import *
STATUS_NEW = 1
STATUS_READY = 2

'''
Если вы не хотите прикасаться к более старой миграции, 
сначала вы можете сделать makemigrations --empty appname, 
чтобы сначала создать пустую миграцию. 
Затем запустите makemigrations, который создаст другую миграцию с
о всеми изменениями. 
Переместите уже сделанные миграции в пустую миграцию, 
которую вы создали.. затем --fake тот. Теперь django понимает, 
как выглядит база данных, будет синхронизироваться с реальностью, 
и вы можете migrate как обычно, применяя изменения в последнем файле миграции.
python manage.py makemigrations --empty aparser
python manage.py migrate --fake-initial
python manage.py makemigrations
python manage.py migrate

python manage.py migrate aparser zero
python manage.py migrate
python manage.py makemigrations
#######################################################


        Restore the database in Postgres database (used pgAdmin tool for this)
        (virtualenv)python manage.py loaddata dumpfile.json
        Dropping django_migrations table from database (used pgAdmin tool for this)
        (virtualenv)python manage.py makemigrations
        (virtualenv)python manage.py migrate --fake
        (virtualenv)python manage.py migrate
        (virtualenv)python manage.py collectstatic
        (virtualenv)python manage.py runserver 0.0.0.0:8000


'''

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
    #url_path
    #url_path1 = models.CharField(verbose_name='Region', max_length=255, blank=True)

    slug_reg = models.CharField(verbose_name='region', max_length=255, blank=True)
    reg_kod = models.IntegerField('Region_kod', blank=True)

    slug_city = models.CharField(verbose_name='City', max_length=255, blank=True)
    city_kod = models.IntegerField('City_kod', blank=True)

    slug_category = models.CharField(verbose_name='category', max_length=255, blank=True)
    category_kod = models.IntegerField('category_kod', blank=True)

    search_key = models.CharField(verbose_name='search_key', max_length=255, blank=True)
    search_filter = models.CharField(verbose_name='search_filter', max_length=255, blank=True)

    search_parametrs_web = models.CharField(verbose_name='search_parametrs_web', max_length=255, blank=True)
    search_parametrs_api = models.CharField(verbose_name='search_parametrs_api', max_length=255, blank=True)

    search_memo = models.CharField(verbose_name='search_memo', max_length=255, blank=True)

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
    published_date = models.DateTimeField(verbose_name='Дата публикации', blank=True, null=True) #default=datetime.datetime.now(),
    #published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', blank=True, null=True)
    # image_url = models.URLField()
    date_upgrade = models.DateTimeField(verbose_name='Дата изменения', blank=True, null=True) #default=datetime.date
    seller_url = models.URLField(verbose_name='Продавец', blank=True, unique=False)

    timestamp = models.DateTimeField(verbose_name='штамп запроса', blank=True, null=True) #default=datetime.date

    def __str__(self):
        return f'#{self.pk} {self.title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


# class path_xpath(models.Model):
#     path_name = models.TextField(
#         verbose_name='Название поля',
#         blank=True,
#         unique=False,
#     )
#     path_str = models.TextField(
#         verbose_name='XPATH',
#         blank=True,
#         unique=False,
#     )

class Category(models.Model):
    cat_kod = models.IntegerField('kod')
    name = models.CharField(verbose_name='Категория', max_length=255, blank=True)
    parent_kod = models.IntegerField('Родитель', blank=True)
    slug = models.CharField(max_length=255, blank=True)
    #url_path1 = models.CharField(max_length=255, blank=True)
    url_name = models.CharField(verbose_name='altername', max_length=255, blank=True)


class Region(models.Model):
    #region_id = models.IntegerField('kod_id')
    kod_region = models.CharField('код авто', max_length=255, blank=True)
    name = models.CharField('Регион', max_length=255, blank=True)
    name_const = models.CharField('по конституции', max_length=255, blank=True)
    slug = models.CharField(verbose_name='Slug', max_length=255, blank=True)
    #url_path1 = models.CharField(verbose_name='URL_path', max_length=255, blank=True)
    url_name = models.CharField(verbose_name='URL_name', max_length=255, blank=True)
    subject_kod = models.CharField(verbose_name='subject_kod', max_length=255, blank=True)
    phone_kod = models.CharField(verbose_name='phone_kod', max_length=255, blank=True)
    index_post = models.IntegerField(verbose_name='почтовый индекс', blank=True)

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return self.name

class City(models.Model):
    # avito_id = models.IntegerField('ID')
    city_id = models.IntegerField('kod_id', null=True)
    name = models.CharField(verbose_name='Нас пункт', max_length=255, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Регион')#, null=True)
    # region = models.IntegerField(verbose_name='Регион', blank=True) #models.ForeignKey(Region.region_id, on_delete=models.CASCADE, verbose_name='Регион')
    parent_kod = models.IntegerField(blank=True, null=True)
    slug = models.CharField(verbose_name='Slug', max_length=255, blank=True, null=True)
    #url_path1 = models.CharField(verbose_name='url_path', max_length=255, blank=True, null=True)
    url_name = models.CharField(verbose_name='altername', max_length=255, blank=True, null=True)
    index_post = models.IntegerField('index_post', blank=True, null=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


# class City1(models.Model):
#     # avito_id = models.IntegerField('ID')
#     city_id = models.IntegerField('kod_id', null=True)
#     name = models.CharField(verbose_name='Нас пункт', max_length=255, blank=True, null=True)
#     region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Регион')#, null=True)
#     # region = models.IntegerField(verbose_name='Регион', blank=True) #models.ForeignKey(Region.region_id, on_delete=models.CASCADE, verbose_name='Регион')
#     #parent_kod_ = models.IntegerField(blank=True, null=True)
#     url_path = models.CharField(verbose_name='URL_path', max_length=255, blank=True)
#     url_name = models.CharField(verbose_name='altername', max_length=255, blank=True)
#     index_post = models.IntegerField('index_post', blank=True, null=True)
#
#     class Meta:
#         verbose_name = 'City'
#         verbose_name_plural = 'Cities'
#
#     def __str__(self):
#         return self.name
#
# class City2(models.Model):
#     # avito_id = models.IntegerField('ID')
#     city_id = models.IntegerField('kod_id', null=True)
#     name = models.CharField(verbose_name='Нас пункт', max_length=255, blank=True, null=True)
#     region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Регион')#, null=True)
#     # region = models.IntegerField(verbose_name='Регион', blank=True) #models.ForeignKey(Region.region_id, on_delete=models.CASCADE, verbose_name='Регион')
#     #parent_kod_ = models.IntegerField(blank=True, null=True)
#     url_path = models.CharField(verbose_name='URL_path', max_length=255, blank=True)
#     url_name = models.CharField(verbose_name='altername', max_length=255, blank=True)
#     index_post = models.IntegerField('index_post', blank=True, null=True)
#
#     class Meta:
#         verbose_name = 'City'
#         verbose_name_plural = 'Cities'
#
#     def __str__(self):
#         return self.name
