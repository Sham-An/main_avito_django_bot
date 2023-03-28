# авито парсер на питончике ._py
#!!! json категории + url_path city
# https://m.avito.ru/api/2/search/main?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&locationId=652120

#api/1 Локации Наименование области : id, нас. пункта : id
#{"status":"ok","result":{"locations":[{"parent":{"names":{"1":"Ростовская область"},"id":651110},"names":{"1":"Тарасовский"},"id":652120},{"names":{"1":"Ростовская область"},"id":651110},{"names":{"1":"Все регионы"},"id":621540}]}}
#https://m.avito.ru/api/1/slocations?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&locationId=621540&limit=10&q=%D0%A2%D0%B0%D1%80%D0%B0%D1%81%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9

#api/2/ Категории полный список, locationId=652120, "uri_mweb":"/shops/tarasovskiy"}
#https://m.avito.ru/api/2/search/main?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&locationId=652120

# https://m.avito.ru/api/9/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&categoryId=9&params%5B1283%5D=14756&locationId=640000&params%5B110000%5D=329273&withImagesOnly=1&page=1&lastStamp=1611316560&display=list&limit=30
# !!!! Categories from location https://m.avito.ru/api/2/search/main?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&locationId=650400
#locationId=650400
#"shops":{"title":"Магазины на Авито","uri":"ru.avito://1/shops/search?locationId=650400","uri_mweb":"/shops/kazan"}}

#locationId=651110
#"shops":{"title":"Магазины на Авито","uri":"ru.avito://1/shops/search?locationId=651110","uri_mweb":"/shops/rostovskaya_oblast"}}

##!!!!!!!!!!!  OK Categories https://m.avito.ru/api/1/items/search/header?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&categoryId=9
import requests
from urllib.parse import quote
from urllib.parse import unquote
from datetime import datetime
from math import floor
from time import sleep
import ssl
from requests.adapters import HTTPAdapter
#from requests.packages.urllib3.poolmanager import PoolManager
from urllib3.poolmanager import PoolManager
#from requests.packages.urllib3.util import ssl_
from urllib3.util import ssl_
from time import time
import warnings
import json

warnings.filterwarnings("ignore")
CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""


class TlsAdapter(HTTPAdapter):

    def __init__(self, ssl_options=0, **kwargs):
        self.ssl_options = ssl_options
        super(TlsAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
        self.poolmanager = PoolManager(*pool_args, ssl_context=ctx, **pool_kwargs)


class HttpParser:
    REGION_INFO = 'region_info'
    CATEGORIES_INFO = 'categories_info'
    AVITO_MAIN = 'avito_main'

    avito_urls = {
        'region_info': 'https://m.avito.ru/api/1/slocations?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&locationId=621540&limit=10&q=',
        'categories_info': 'https://m.avito.ru/api/2/search/main?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&locationId=',
        'avito_main': 'https://avito.ru'
    }
#categories_info': &locationId=652000 uri_mweb адрес локации "/shops/rostov-na-donu"
    def __init__(self):
        pass

    @staticmethod
    def get_json_by_request(url):

        cookie = '__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=ef757cc130c5cd228be88e869369c654.1610912291; _ga=GA1.2.559434019.1610912292; _gid=GA1.2.381990959.1610912292; _fbp=fb.1.1610912292358.1831979940; u=2oiycodt.1oaavs8.dyu0a4x7fxw0; v=1610912321; buyer_laas_location=641780; buyer_location_id=641780; luri=novosibirsk; buyer_selected_search_radius4=0_general; buyer_local_priority_v2=0; sx=H4sIAAAAAAACAxXLQQqAIBAF0Lv8dYvRLEdvU0MIBU0iKCHePXr71zGfefd1W5RLYick2kSakiB2VETclpf85n19RJMSp4vJOSlM%2F2BMOBDNaigE9taM8QH0oydNVAAAAA%3D%3D; dfp_group=100; _ym_uid=1610912323905107257; _ym_d=1610912323; _ym_visorc_34241905=b; _ym_isad=2; _ym_visorc_419506=w; _ym_visorc_188382=w; __gads=ID=2cff056a4e50a953-22d0341a94b900a6:T=1610912323:S=ALNI_MZMbOe0285QjW7EVvsYtSa-RA_Vpg; f=5.8696cbce96d2947c36b4dd61b04726f1a816010d61a371dda816010d61a371dda816010d61a371dda816010d61a371ddbb0992c943830ce0bb0992c943830ce0bb0992c943830ce0a816010d61a371dd2668c76b1faaa358c08fe24d747f54dc0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b978e38434be2a23fac7b9c4258fe3658d831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013a20f3d16ad0b1c5462da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bdf0c77052689da50d2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab91e52da22a560f5503c77801b122405c48ab0bfc8423929a6d7a5083cc1669877def5708993e2ca678f1dc04f891d61e35b0929bad7c1ea5dec762b46b6afe81f200c638bc3d18ce60768b50dd5e12c30e37135e8f7c6b64dc9f90003c0354a346b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7acf8b817f3dc0c3f21c1eac53cc61955882da10fb74cac1eab2da10fb74cac1eab5e5aa47e7d07c0f95e1e792141febc9cb841da6c7dc79d0b'

        headers = {'Host': 'm.avito.ru',
                   'pragma': 'no-cache',
                   'cache-control': 'no-cache',
                   'upgrade-insecure-requests': '1',
                   'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
                   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                   'sec-fetch-site': 'none',
                   'sec-fetch-mode': 'navigate',
                   'sec-fetch-user': '?1',
                   'sec-fetch-dest': 'document',
                   'accept-language': 'ru-RU,ru;q=0.9', }

        session = requests.session()
        adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
        session.mount("https://", adapter)
        headers['cookie'] = cookie
        session.headers.update(headers)  # Сохраняем заголовки в сессию
        session.get('https://m.avito.ru/')  # , proxies=proxiess)
        url_api_9 = 'https://m.avito.ru/api/9/items'

        session = requests.session()
        adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
        session.mount("https://", adapter)

        # r = session.request('GET', 'https://www.avito.ru')

        try:
            # resp = requests.get(
            #     url, verify=False
            # )
            resp = session.request('GET', url, verify=False)
            # requests.get(
            # url, verify=False
            # )

            json_content = resp.json()
            if 'status' in json_content.keys():
                if json_content['status'] == 'internal-error':
                    print('internal-error')
                    HttpParser.get_json_by_request(url)
            return json_content
        except requests.exceptions.ProxyError:
            sleep(0.001)
            HttpParser.get_json_by_request(url)

    @staticmethod
    def get_region_id_by_name(region_name):
        #print(f'region_name)
        path_content = (f'{HttpParser.avito_urls[HttpParser.REGION_INFO]}{quote(region_name)}')
        print(f'path_content = {path_content}')
        json_content = HttpParser.get_json_by_request(
            f'{HttpParser.avito_urls[HttpParser.REGION_INFO]}{quote(region_name)}')
        locations = json_content['result']['locations']

        print(f'region_name json_content = {json_content} locations[0]id = {locations[0]["id"]}')
        print(f'region_name = {region_name} locations[0]id = {locations[0]["id"]}')
        return locations[0]['id']

    @staticmethod
    def get_category_link_by_id(region_id, category_id):
        # !!!! Categories from location https://m.avito.ru/api/2/search/main?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&locationId=650400'
        time = floor(datetime.timestamp(datetime.now().replace(second=0, microsecond=0)))
#       resp = session.get(url_api_9, params=params)  # , proxies = proxiess)
        url_json_items = 'https://m.avito.ru/api/9/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&'
        url_json = 'https://m.avito.ru/api/2/search/main?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&locationId = 650400'
        url_json = 'https://m.avito.ru/api/2/search/main?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&location' #Id = 650400
        url_json_param = f'lastStamp={time}&locationId={region_id}&categoryId={category_id}&page=1&display=list&limit=1'

        #with open("avito_category.json", encoding='utf-8') as file:
          # json_content = json.load(file)
            # list_dict(data)
            #list_category(data)
            #print(f'region_id === {region_id}')
         #   print(f'category_id === {category_id}')
            #print(f'json_content === {json_content}')


        # json_content = HttpParser.get_json_by_request(
        #     'https://m.avito.ru/api/2/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&'
        #     f'lastStamp={time}&locationId={region_id}&categoryId={category_id}&page=1&display=list&limit=1'
        # )
        # print(f'url_json OK!!! = {url_json}\n url_json_param = {url_json_param}')
#!!!!!!!!!!!  OK Categories           https://m.avito.ru/api/1/items/search/header?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&categoryId=9
        #'https://m.avito.ru/api/9/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&lastStamp=1663083720&locationId=650400&categoryId=1&page=1&display=list&limit=1'
        #json_content = HttpParser.get_json_by_request('https://m.avito.ru/api/9/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&lastStamp=1663083720&locationId=650400&categoryId=1&page=1&display=list&limit=1')
        # category_id_locations.json 'https://m.avito.ru/api/4/items/search/header?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&categoryId=9'
        json_content = HttpParser.get_json_by_request('https://m.avito.ru/api/2/search/main?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&locationId=652000')#650400')

        #     'https://m.avito.ru/api/9/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&'
        #     f'lastStamp={time}&locationId={region_id}&categoryId={category_id}&page=1&display=list&limit=1'
        #)

        if json_content is None:
            return None

        print(f'!!! json_content = {json_content}')

        #item = json_content['result']['seo']
        #item = json_content['result']['seo']
        #link = item['canonicalUrl']

        #return link
        return None

    @staticmethod
    def get_sub_categories_by_id(region_id, category_id):
        if category_id == 9:  # Skip automobiles category
            return

        time = floor(datetime.timestamp(datetime.now().replace(second=0, microsecond=0)))

        #OK https://m.avito.ru/api/1/items/search/header?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&categoryId=9
        json_content = HttpParser.get_json_by_request(
            'https://m.avito.ru/api/1/items/search/header?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&'
            f'parameters[locationId]={region_id}&parameters[categoryId]={category_id}'
        ) #lastStamp={time}&
        filters = json_content['result']['filters']

        for sub_category_item in filters:

            if sub_category_item['id'] not in ['shortcut']:  # JUST RUINED MY CODE
                continue

            sub_category_name = sub_category_item['title']
            # print(f'sub_category: {sub_category_item}')
            sub_category_link = f'{HttpParser.avito_urls[HttpParser.AVITO_MAIN]}{sub_category_item["value"]["url"]}'

            yield sub_category_name, sub_category_link

    @staticmethod
    def get_all_categories_by_region_id(reg_id):
        region_id=reg_id
        #?https://m.avito.ru/api/4/items/search/header?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&regiononId=650400&categoryId=9
        print(f'!!! OK HttpParser.avito_urls[HttpParser.CATEGORIES_INFO] == {HttpParser.avito_urls[HttpParser.CATEGORIES_INFO]}{region_id}')
        json_content = HttpParser.get_json_by_request(f'{HttpParser.avito_urls[HttpParser.CATEGORIES_INFO]}{region_id}')
        main_categories = json_content['categories']
        print(f'main_categories = = {main_categories}')

        output_categories = {}

        for parent_category in main_categories[1:]:
            parent_id = parent_category['id']
            parent_name = parent_category['name']

            category_link = HttpParser.get_category_link_by_id(region_id, parent_id)
            print(f'category_link = = {category_link}')

            if category_link is not None:
                output_categories[parent_name] = {
                    'id': parent_id,
                    'link': category_link
                }

            for child_category in parent_category['children']:
                child_id = child_category['id']
                child_name = child_category['name']

                child_category_link = HttpParser.get_category_link_by_id(region_id, child_id)

                if child_category_link is not None:
                    output_categories[child_name] = {
                        'id': child_id,
                        'link': child_category_link
                    }

                for sub_category_name, sub_category_link in HttpParser.get_sub_categories_by_id(region_id, child_id):
                    output_categories[sub_category_name] = {
                        'id': None,
                        'link': sub_category_link
                    }

        return output_categories

    @staticmethod
    def get_add_json_info_by_id(add_id):
        add_id = "2953844958"
        print(f'https://m.avito.ru/api/19/items/{add_id}?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir')
        json_content = HttpParser.get_json_by_request(
            f'https://m.avito.ru/api/14/items/{add_id}?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
        )

        return json_content

    @staticmethod
    def get_phone_number_by_add_id(add_id):
        json_content = HttpParser.get_json_by_request(
            f'https://m.avito.ru/api/1/items/{add_id}/phone?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
        )

        return unquote(json_content['result']['action']['uri'].split('=')[-1])

    @staticmethod
    def get_add_info_by_id(add_id):
        add_json_info = HttpParser.get_add_json_info_by_id(add_id)

        del add_json_info['contacts']

        add_json_info['seller']['connection']['sources'][0]['type'] = HttpParser.get_phone_number_by_add_id(add_id)

        return add_json_info

    @staticmethod
    def get_adds_list(category_name_for_search, region_id, categories_dict, limit_shows=1):
        time = floor(datetime.timestamp(datetime.now().replace(second=0, microsecond=0)))

        adds_list = []

        for category_name in categories_dict.keys():
            if category_name_for_search not in category_name:
                continue

            category = categories_dict[category_name]
            category_id = category['id']
            category_link = category['link']
            orig_uri = category_link.replace(HttpParser.avito_urls[HttpParser.AVITO_MAIN], '')

            if category_id is None:
                json_content = HttpParser.get_json_by_request(
                    'https://m.avito.ru/api/9/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&'
                    f'page=1&lastStamp={time}&display=list&limit={limit_shows}&url={orig_uri}'
                )
            else:
                json_content = HttpParser.get_json_by_request(
                    'https://m.avito.ru/api/9/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&'
                    f'locationId={region_id}&categoryId={category_id}&page=1&display=list&limit={limit_shows}'
                )
#https://m.avito.ru/api/9/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&locationId=622470&categoryId=14&page=1&display=list'

            items = json_content['result']['items']

            for item in items:
                if 'type' in item.keys() and item['type'] == 'vip':
                    add_id = item['value']['list'][0]['value']['id']
                else:
                    add_id = item['value']['id']

                add_json_info = HttpParser.get_add_json_info_by_id(add_id)

                del add_json_info['contacts']

                add_json_info['seller']['connection']['sources'][0]['type'] = HttpParser.get_phone_number_by_add_id(
                    add_id)

                adds_list.append(add_json_info)

        return adds_list


session = requests.session()
adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
session.mount("https://", adapter)

#region_id = HttpParser.get_region_id_by_name('Казань')
#region_id = HttpParser.get_region_id_by_name('Тарасовский')
#print(region_id)
add_id = "2953844958"
items_id = HttpParser.get_add_json_info_by_id(add_id)
print(items_id)
#https://m.avito.ru/api/19/items/2819341808?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&action=view&context=H4sIAAAAAAAA_0q0MrSqLrYytFKqULIutjI2tFIyLzQ1NDTOySmwNDLKLqrMykpMKykpNzMpMchPS7LMVLKuBQQAAP__uJ4eMzUAAAA

#all_categories = HttpParser.get_all_categories_by_region_id(region_id)
    #all_adds = HttpParser.get_adds_list('Мотоциклы и мототехника', region_id, all_categories, limit_shows=50)
#example_add = HttpParser.get_add_info_by_id('2778802474')


print(f'all_categories')
# print(f'all_adds')
#print(f'example_add')

# Telegram: @xmm_0
