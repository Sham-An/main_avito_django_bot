import datetime
import json
#https://wordstat.yandex.ru/#!/?words=%D0%BA%D0%BE%D0%BC%D0%BF
#https://tools.pixelplus.ru/news/podskazki-avito
#######################################
#!!!!!DIR TO LIST !!!!!!
#parts = urlparse(url)
#print(parts)
#directories = parts.path.strip('/').split('/')
#print(directories)


import os
import ssl

import requests
# https://www.avito.ru/rostovskaya_oblast/mototsikly_i_mototehnika?cd=1&f=ASgCAgECAUXGmgwXeyJmcm9tIjoyMDAwLCJ0byI6NzAwMH0&q=скутер&s=1
#
from lxml import html
##########################################
from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.poolmanager import PoolManager
from urllib3.poolmanager import PoolManager
# from requests.packages.urllib3.util import ssl_
from urllib3.util import ssl_
from fake_useragent import UserAgent
from urllib.parse import urlparse

# ua = UserAgent()

# Идентификация элемента с помощью функций XPath по тексту
# Поскольку у нас есть видимый текст «Log in to Twitter», мы могли бы использовать следующие функции XPath для идентификации уникального элемента.
# contains() [по тексту] //h1[contains(text(),’ Log in to’)]
# Поиск по частичному значению атрибута кнопка
# //input[contains(@value,’Feeling’)]
# поиск по содержимому атрибута Name //input[contains(@name=’btnI’)]

# starts-with() [по тексту] //h1[starts-with(text(),’Log in’)] starts-with()
# в сочетании с атрибутом может пригодиться для поиска элементов,
# у которых начало атрибута постоянное, а окончание изменяется.

# text() //h1[text()='Log in']
# Функции XPath, такие как contains(), starts-with() и text(), при использовании с текстом «Log in to Twitter» помогут нам корректно идентифицировать элемент, после чего мы сможем произвести над ним дальнейшие операции.

ua = UserAgent(browsers=['edge', 'chrome'])
ua_str = ua.random
print(ua_str)
CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""

key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'  # ключ, с которым всё работает, не разбирался где его брать, но похоже он статичен, т.к. гуглится на различных форумах
cookie = '__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=ef757cc130c5cd228be88e869369c654.1610912291; _ga=GA1.2.559434019.1610912292; _gid=GA1.2.381990959.1610912292; _fbp=fb.1.1610912292358.1831979940; u=2oiycodt.1oaavs8.dyu0a4x7fxw0; v=1610912321; buyer_laas_location=641780; buyer_location_id=641780; luri=novosibirsk; buyer_selected_search_radius4=0_general; buyer_local_priority_v2=0; sx=H4sIAAAAAAACAxXLQQqAIBAF0Lv8dYvRLEdvU0MIBU0iKCHePXr71zGfefd1W5RLYick2kSakiB2VETclpf85n19RJMSp4vJOSlM%2F2BMOBDNaigE9taM8QH0oydNVAAAAA%3D%3D; dfp_group=100; _ym_uid=1610912323905107257; _ym_d=1610912323; _ym_visorc_34241905=b; _ym_isad=2; _ym_visorc_419506=w; _ym_visorc_188382=w; __gads=ID=2cff056a4e50a953-22d0341a94b900a6:T=1610912323:S=ALNI_MZMbOe0285QjW7EVvsYtSa-RA_Vpg; f=5.8696cbce96d2947c36b4dd61b04726f1a816010d61a371dda816010d61a371dda816010d61a371dda816010d61a371ddbb0992c943830ce0bb0992c943830ce0bb0992c943830ce0a816010d61a371dd2668c76b1faaa358c08fe24d747f54dc0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b978e38434be2a23fac7b9c4258fe3658d831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013a20f3d16ad0b1c5462da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bdf0c77052689da50d2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab91e52da22a560f5503c77801b122405c48ab0bfc8423929a6d7a5083cc1669877def5708993e2ca678f1dc04f891d61e35b0929bad7c1ea5dec762b46b6afe81f200c638bc3d18ce60768b50dd5e12c30e37135e8f7c6b64dc9f90003c0354a346b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7acf8b817f3dc0c3f21c1eac53cc61955882da10fb74cac1eab2da10fb74cac1eab5e5aa47e7d07c0f95e1e792141febc9cb841da6c7dc79d0b'


#############################

class TlsAdapter(HTTPAdapter):

    def __init__(self, ssl_options=0, **kwargs):
        self.ssl_options = ssl_options
        super(TlsAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
        self.poolmanager = PoolManager(*pool_args, ssl_context=ctx, **pool_kwargs)


def parse_xml_new(resp_text):
    html_txt = resp_text  # response.text
    #print(html_txt)

    #Blok
    #path = './/div//div//div//ul[@data-marker="rubricator/list"]'
    #path = './/div//div//div//ul[@data-marker="rubricator/list"]//ul//a[substring(@class,1,25) ="rubricator-list-item-link"]'
    #path_items = './/a[substring(@class,1,25) ="rubricator-list-item-link"]'
    #path_items_full = './/div//div//div//ul[@data-marker="rubricator/list"]//ul//a[substring(@class,1,25) ="rubricator-list-item-link"]'
    #.//div//div//div[@data-marker='rubricator']//i//a[substring(@class,1,25) ="rubricator-list-item-link"]
    #.//div//div//div[@data-marker="rubricator"]//a[substring(@class,1,25) ="rubricator-list-item-link"]
    #a[substring(@href,1,21) ="https://www.avito.ru/"]
    #Исключить data-category-mc-id="3838"  data-marker="category[1003838]/link"
    #          data-category-mc-id="354"   data-marker="category[1000354]/link"
    #path_name_cat = './/text()'
    path_url = '//a[@href]'
    path_pages = './/div//div[@data-marker="more-popup"] //a[substring(@class,1,9) ="link-link"]//text()'
    path_url = './/div//div[@data-marker="more-popup"] //a[substring(@class,1,9) ="link-link"]//text()'
    var = 'Автомобили'
    # .//div//div[@data-marker="more-popup"]//a[text()='Автомобили']
    path_use_var = (f'.//div//div[@data-marker="more-popup"]//a[text()={var}')

    ##!!!!!!!####!!!!!!###!!!!#БОМБА ## БОМБА ## БОМБА ## БОМБА ## БОМБА ## БОМБА ## БОМБА ## БОМБА
    # substring(@class,1,13) ="iva-item-text"
    # starts-with(string, string) https://habr.com/ru/company/otus/blog/533354/
    # Поиск по тексту:
    # //h1[contains(text(),’ Log in to’)]
    # //h1[contains(text(),’ in to Twitter’)]
    # path_pages = '//div[contains(@class, "pagination-root")]/span[last()-1]/text()'
    # !Не наша деревня поиска OK! path_location = './/span[contains(@class, "geo-addr")]/span/text()'
    path = './/div//div//div//ul[@data-marker="rubricator/list"]//ul//a[substring(@class,1,25) ="rubricator-list-item-link"]'
    #path_items_full = './/div//div//div//ul[@data-marker="rubricator/list"]//ul//a[substring(@class,1,25) ="rubricator-list-item-link"]'
    path_items_full = './/div//div//div//ul[@data-marker="rubricator/list"]//ul//a[@data-category-id>"0"]'
    path_name_cat = './/text()'
    #    path_url = '//a[@href]'
    path_name_cat = './/text()'
    path_url = './/@href'
    path_cat_id = './/@data-category-id'
    stop1 = 'evaluation'
    stop2 = 'catalog '

    # path_pages = path+path_name_cat
    # tree = html.fromstring(html_txt)
    # count_page = tree.xpath(path)
    # print(count_page)

    tree = html.fromstring(html_txt)


    for item in tree.xpath(path_items_full): #html.fromstring(html_txt):

        name = item.xpath(path_name_cat)
        cat_id = item.xpath(path_cat_id)
        url = item.xpath(path_url)#[0]
        url_pars1 = urlparse(url[-1])
        path_url1 = url_pars1[2]
        dirLst = path_url1.split("/")
        dirname_city1 = dirLst[1]
        dirname_cat1 = dirLst[2]
        if (stop1 in dirname_city1) or ((stop2 in dirname_city1)) or (len(dirLst) < 3):
            return

        print(f'dirLst {len(dirLst)} = {dirLst}  url = {url}')
        print(f'  name {name} @@@@@@@@ Cat_id = {cat_id}      dirname_cat = {dirname_cat1} \n')
##########################################################################
        #print(f'dirname = {dirname1}')
    # ! В HTML карточке объявления путь к ID City
    # https://www.avito.ru/bryansk/zapchasti_i_aksessuary/dvigatel_na_skuter_150_kubov_157qmj_2332435829
    # //*[@id="app"]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div/div[3]
    # XPATH = .//div//div//div[@data-map-type='dynamic']

    # data-item-id="2332435829" ID объявления
    # data-location-id="623880" ID City
    # data-category-id="10" ID Kategory


    #tree = html.fromstring(html_txt)
    #index = 0

    # for item in tree.xpath(path_item):  # .getall():
    #     # for item in tree.xpath(path_location):  # .getall():
    #     item_id = item.xpath(path_id)
    #     print(f'ITEM_ID {item.xpath(path_id)[0]} type{type(item_id)} {item.xpath(path_id)[0]}')
    #     name = item.xpath(path_name)[0]
    #     price = item.xpath(path_price)
    #     location = item.xpath(path_location)
    #     location_free = item.xpath(path_location_free)
    #     print(location_free)
    #     print(f'!!!!!!!!!!!!NAME {name} @@@@ ЦЕНА {price} Location {location}')
    #     index += 1
    #     title = item.xpath(path_title)[0]
    #     print(f' {index} title = {title}')
    #     print(datetime.datetime.now())

    # list_lxml = tree.xpath(path)[0]
    # for item_lxml in items_lxml:
    #     desript = item_lxml.xpath('//meta[@itemprop="description"]')
    #     # getting movie id
    #     movie_link = item_lxml.xpath('.//div[@class = "nameRus"]/a/@href')[0]
#<div class="style-item-map-wrapper-ElFsX" data-map-zoom="16" data-map-lat="53.233451" data-map-lon="34.358116" data-map-type="dynamic" data-item-id="2140356688" data-location-id="623880" data-category-id="10" data-shop-id="1481543">
def parse_xml_old(resp_text):
    html_txt = resp_text  # response.text
    #print(html_txt)

    path = './/div//div[@data-marker="more-popup"]//a[substring(@class,1,9)="link-link"]/@href'
    path = './/div//div[@data-marker="more-popup"]//a[substring(@class,1,9)="link-link"]'
    path__ = './/div//div[@data-marker="more-popup"]//a[substring(@href,1,33)="https://www.avito.ru/tarasovskiy/"]'
    path___ = './/div//div[@data-marker="more-popup"]//div[substring(@class,1,30)="old-rubricator-content-columns"]'
    path____ ='.//div//div[@data-marker="more-popup"]//div[substring(@class,1,30)="old-rubricator-content-columns"]//li'
    path_name_cat = './/text()'
    path_url = '//a[@href]'
    path_pages = './/div//div[@data-marker="more-popup"] //a[substring(@class,1,9) ="link-link"]//text()'
    path_url = './/div//div[@data-marker="more-popup"] //a[substring(@class,1,9) ="link-link"]//text()'
    var = 'Автомобили'
    # .//div//div[@data-marker="more-popup"]//a[text()='Автомобили']
    path_use_var = (f'.//div//div[@data-marker="more-popup"]//a[text()={var}')

    ##!!!!!!!####!!!!!!###!!!!#БОМБА ## БОМБА ## БОМБА ## БОМБА ## БОМБА ## БОМБА ## БОМБА ## БОМБА
    # substring(@class,1,13) ="iva-item-text"
    # starts-with(string, string) https://habr.com/ru/company/otus/blog/533354/
    # Поиск по тексту:
    # //h1[contains(text(),’ Log in to’)]
    # //h1[contains(text(),’ in to Twitter’)]
    # path_pages = '//div[contains(@class, "pagination-root")]/span[last()-1]/text()'
    # !Не наша деревня поиска OK! path_location = './/span[contains(@class, "geo-addr")]/span/text()'

    path_pages = path+path_name_cat
    tree = html.fromstring(html_txt)
    #count_page = tree.xpath(path_pages)
    count_page = tree.xpath(path)
    print(count_page)
    print(len(count_page))
    tree = html.fromstring(html_txt)

#    path_url = '//a[@href]'
    path_name_cat = './/text()'
    path_url = './/@href'

    for item in tree.xpath(path): #html.fromstring(html_txt):
        #print(item)
    #if count_page:
        name = item.xpath(path_name_cat)
        url = item.xpath(path_url)#[0]
        #!!! GET url все категории https://www.avito.ru/tarasovskiy?q=а
        #!!!! И его уже парсим по категориям
        print(f'Pages names = {name} url = {url}')

    # ! В HTML карточке объявления путь к ID City
    #//*[@id="app"]//div[substring(@class,1,22) ="style-item-map-wrapper"]
    #<div class="style-item-map-wrapper-ElFsX" data-map-zoom="16" data-map-lat="55.751664" data-map-lon="37.817173" data-map-type="dynamic" data-item-id="1488644666" data-location-id="637640" data-category-id="101">
    #//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[3]/div[1]/div[2]/div[1]/div[3]/div/div[3]

#//*[@id="app"]/div/div[3]/div/div[2]/div[3]/div[3]/div[3]/nav/ul/li[7]/span
    #//*[@id="app"]//a[contains(@class, "pagination-page")]

    #Last page
    #//*[@id="app"]//div[contains(@class, "pagination-page")]/a[last()]

    #ID-City = ./div/div/div[substring(@class,1,22) ="style-item-map-wrapper"]
    #"style-item-map-wrapper-ElFsX"
#//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div/div[3]
#!!! //*[@id="app"]//div[substring(@data-marker,1,15) ="item-navigation"]
#data-marker="item-navigation"
#div[substring(@data-marker,1,15) ="item-navigation"]

    # data-item-id="2332435829" ID объявления
    # data-location-id="623880" ID City
    # data-category-id="10" ID Kategory


    #tree = html.fromstring(html_txt)
    #index = 0

    # for item in tree.xpath(path_item):  # .getall():
    #     # for item in tree.xpath(path_location):  # .getall():
    #     item_id = item.xpath(path_id)
    #     print(f'ITEM_ID {item.xpath(path_id)[0]} type{type(item_id)} {item.xpath(path_id)[0]}')
    #     name = item.xpath(path_name)[0]
    #     price = item.xpath(path_price)
    #     location = item.xpath(path_location)
    #     location_free = item.xpath(path_location_free)
    #     print(location_free)
    #     print(f'!!!!!!!!!!!!NAME {name} @@@@ ЦЕНА {price} Location {location}')
    #     index += 1
    #     title = item.xpath(path_title)[0]
    #     print(f' {index} title = {title}')
    #     print(datetime.datetime.now())

    # list_lxml = tree.xpath(path)[0]
    # for item_lxml in items_lxml:
    #     desript = item_lxml.xpath('//meta[@itemprop="description"]')
    #     # getting movie id
    #     movie_link = item_lxml.xpath('.//div[@class = "nameRus"]/a/@href')[0]


################################################################################################
def get_file_new():
    #with open("Data/get_categories1.html", 'r', encoding='utf-8') as file:
    with open("get_categories2.html", 'r', encoding='utf-8') as file:
        r = file.read()
     #   print(r)
    parse_xml_new(r)
    # print(r.text)

def get_file_old():
    #with open("Data/get_categories1.html", 'r', encoding='utf-8') as file:
    with open("Data/get_categories1.html", 'r', encoding='utf-8') as file:
        r = file.read()
     #   print(r)
    parse_xml_old(r)
    # print(r.text)


def main():
    #get_file_old()
    get_file_new()
    # CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""
    # session = requests.session()
    # session2 = requests.session()
    # adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
    # adapter2 = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
    # session.mount("https://", adapter)
    # session2.mount("https://", adapter2)


if __name__ == '__main__':
    main()

# категории + нас. пункт id + URL PATH
# https://m.avito.ru/api/2/search/main?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&locationId=652120

# НЕТ В общем запрсе ID & PATH НЕТУ!
# ! В HTML карточке объявления путь к ID City
# https://www.avito.ru/bryansk/zapchasti_i_aksessuary/dvigatel_na_skuter_150_kubov_157qmj_2332435829
# //*[@id="app"]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div/div[3]
# <div class="style-item-map-wrapper-ElFsX" data-map-zoom="16"
# data-map-lat="53.233451" data-map-lon="34.358116" data-map-type="dynamic"

# data-item-id="2332435829" ID объявления
# data-location-id="623880" ID City
# data-category-id="10" ID Kategory

# API/9 JSON Смотрим после "items"
#    "seoNavigation": {
#       "breadcrumbs": [
#         {
#           "name": "Лабинск",
#           "title": "Все объявления в Лабинске",
#           "url": "/labinsk"
#         },
#         {
#           "name": "Транспорт",
#           "title": "Транспорт в Лабинске",
#           "url": "/labinsk/transport"
#         },
#         {
#           "name": "Автомобили",
#           "title": "Автомобили в Лабинске",
#           "url": "/labinsk/avtomobili"
#         }
#       ]
#     },

# file:///C:/Users/miladmin/Downloads/%D0%9F%D0%B0%D1%80%D1%81%D0%B8%D0%BD%D0%B3/%D0%9F%D0%B0%D1%80%D1%81%20%D0%9A%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3%20%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D0%B5%D0%B9%20_%20%D0%90%D0%B2%D0%B8%D1%82%D0%BE.mhtml
# //*[@id="app"]/div/div[2]/div[2]/span/div
# //*[@id="app"]/div/div[2]/div[2]/span  //div[@data-marker="more-popup"]
# //*[@id="app"]/div//div[@data-marker="more-popup"] //a[substring(@class,1,9) ="link-link"]
# //*[@id="app"]/div//div[@data-marker="more-popup"] //a[substring(@class,1,9) ="link-link"]//
# //*[@id="app"]/div//div[@data-marker="more-popup"] //a[substring(@class,1,9) ="link-link"]//text()='Автомобили'
# //*[@id="app"]/div/div[2]/div[2]/span/div/span/div/div/div/div[1]/div[1]/ul/li[1]/a
