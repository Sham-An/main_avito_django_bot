# Импортируем библиотеку
from lxml import html
import requests

def main():
    print('main')
    # Получаем содержимое страницы
    #url = 'https://www.avito.ru/moskva?q=python'
    url = 'https://www.avito.ru/moskva/odezhda_obuv_aksessuary/zhenskaya_odezhda-ASgBAgICAUTeAtYL'
    response = requests.get(url)
    print(response.status_code)
    page = html.fromstring(response.content)

    # Определяем переменные для путей
    XPATH_BLOCK = '//div[@data-marker="item"]'
    XPATH_TITLE = './/h3[@itemprop="name"]/span[@class="title-root"]/text()'
    XPATH_LINK = './/a[@data-marker="item-title"]/@href'
    XPATH_PRICE = 'normalize-space(.//span[@itemprop="price"])'

    # Выполняем поиск элементов
    items = page.xpath(XPATH_BLOCK)
    print(items)
    # Создаем словарь и сохраняем результаты
    results = {}
    for item in items:
        title = item.xpath(XPATH_TITLE)[0]
        link = item.xpath(XPATH_LINK)[0]
        price = item.xpath(XPATH_PRICE)
        results[title] = {'link': link, 'price': price}
        print(title, '\n', link )

    url = 'https://www.avito.ru/'
    response = requests.get(url)
    html_tree = html.fromstring(response.text)

    for category in html_tree.xpath('//ul[@data-marker="search-form/suggestBar/list/"]//a/text()'):
        print(category)

if __name__ == '__main__':
    main()


'''
Для создания моделей Django для категорий AVITO, вам необходимо создать следующие поля:

1. `title` - название объявления;
2. `url` - URL адрес объявления;
3. `price` - цена объявления;
4. `currency` - валюта цены объявления;
5. `image` - изображение объявления (можно хранить в виде ссылки);
6. `description` - описание объявления;
7. `location` - местоположение объявления.

Пример модели Django для категории автомобилей на AVITO:

python
from django.db import models

class Car(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    image = models.URLField(blank=True, null=True)
    description = models.TextField()
    location = models.CharField(max_length=255)


Пример модели Django для категории квартир на AVITO:

python
from django.db import models

class Flat(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    image = models.URLField(blank=True, null=True)
    description = models.TextField()
    location = models.CharField(max_length=255)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    floor = models.IntegerField()
    rooms = models.IntegerField()
    balcony = models.BooleanField()
    year_built = models.IntegerField()


Обратите внимание, что поля `image` и `description` могут быть опциональными.


Вот пример модели Django для категории "Транспорт" на AVITO:

python
from django.db import models

class AvitoTransport(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    location = models.CharField(max_length=200)
    url = models.URLField()
    image_url = models.URLField()

    def __str__(self):
        return self.title


В этом примере мы создаем модель `AvitoTransport` с полями `title`, `description`, `price`, `location`, `url` и `image_url`, которые соответствуют полям, которые можно получить из страницы объявления на AVITO. 

- `title` - название объявления
- `description` - описание объявления
- `price` - цена
- `location` - местоположение
- `url` - ссылка на объявление
- `image_url` - ссылка на изображение

Метод `__str__()` определяет, как будет выглядеть объект в строковом формате, если, например, мы используем данную модель в интерфейсе администрирования Django.

Это только базовый пример, в зависимости от типа категории на AVITO и конкретных требований к проекту, поля могут отличаться.

Для регионов модель можно создать следующим образом:
Пример модели Django для населенных пунктов на AVITO:

python
from django.db import models


class Region(models.Model):
    title = models.CharField('Название', max_length=255)
    avito_id = models.IntegerField('ID на Avito')
    
    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
        
    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField('Название', max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Регион')
    avito_id = models.IntegerField('ID на Avito')
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        
    def __str__(self):
        return self.title


Объект `Region` представляет собой регион на Avito, а `City` — населенный пункт внутри этого региона. Каждый регион и населенный пункт имеет название и числовой идентификатор на Avito. С помощью связи `ForeignKey` модель города связана с моделью региона.

#####################################

Пакет `psiphon3` предоставляет возможность использования функций и создания соединения с помощью кода Python. Более подробно можно ознакомиться с документацией по ссылке https://github.com/Psiphon-Labs/psiphon-tunnel-core-python.

Вот пример использования `psiphon3` в Python:


from psiphon3 import PsiphonTunnelCore

proxy_host = "&lt;адрес_прокси_сервера>"
proxy_port = &lt;порт_прокси_сервера>
app_id = "&lt;идентификатор_приложения>"
config = {
    "psiphon": {
        "upstream_proxy": "http://{}:{}".format(proxy_host, proxy_port),
        "app_id": app_id
    }
}

tunnel = PsiphonTunnelCore.create(config)

if tunnel.allocate():
    print("Connected to Psiphon server")
    # Use tunnel for requests
else:
    print("Connection unsuccessful")

'''