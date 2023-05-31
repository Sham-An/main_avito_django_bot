import json
import sqlite3
import time
from datetime import datetime
import requests
#from realty_tmp import check_database
from realty_tmp import check_database
#from a
from requests.adapters import HTTPAdapter
#from requests.packages.urllib3.poolmanager import PoolManager
from urllib3.poolmanager import PoolManager
#from requests.packages.urllib3.util import ssl_
from urllib3.util import ssl_
from datetime import datetime
#from realty import check_database

import ssl
import requests

CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""

class TlsAdapter(HTTPAdapter):

    def __init__(self, ssl_options=0, **kwargs):
        self.ssl_options = ssl_options
        super(TlsAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
        self.poolmanager = PoolManager(*pool_args, ssl_context=ctx, **pool_kwargs)

# session = requests.session()
# adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
# session.mount("https://", adapter)
#
# try:
#     r = session.request('GET', 'https://www.avito.ru')
#     print(r.text)[1000]
# except Exception as exception:
#     print(exception)


def get_offer(item):

    offer = {}
#    id
    id_item = item["id"]
    offer["offer_id"] = id_item
#    id_item
    offer["id_item"] = id_item
#    category_name
    offer["category_name"] = ''
#    category_kod
    offer["category_kod"] = ''
#    date
    time_item = item['time']
    timestamp = datetime.fromtimestamp(time_item)
    timestamp = datetime.strftime(timestamp, '%Y-%m-%d %H:%M:%S')
    offer["date"] = timestamp
#    time
    offer["time"] = time_item
#    title_desk
    title = 'Error title'#item['title'].split(', ')
    rooms = title[0]
    #area = float(title[1].replace(' м²', '').replace(',', '.'))
    area = '100'#float(title[1].replace(',', '.'))
    print(f'area     {area}')
    #title = item['title']
    offer["title_desk"] = title
#    title_full
    offer["title_full"] = title #item['title']
#    img
    offer["img"] = ''
#    price
    price = ''.join(item['price'].replace(' ₽ в месяц', '').split())
    offer["price"] = price
#    address
    offer["address"] = f"{item['location']}, {item['address']}"
#    coords
    offer["coords"] = ''
    #    url
    url_item = "https://www.avito.ru" + item["uri_mweb"]
    offer["url"] = url_item #"https://www.avito.ru" + item["uri_mweb"]
#    uri
    offer["uri"] = ''
#    uri_mweb
    offer["uri_mweb"] = url_item
#    offer_id
    offer["offer_id"] = id_item
#    area
    offer["area"] = area
#    rooms
    offer["rooms"] = rooms
#    floor
    floor_info = title[2].replace(' эт.', '').split('/')
    floor = floor_info[0]
    total_floor = floor_info[-1]
    offer["floor"] = floor
#    total_floor
    offer["total_floor"] = total_floor



#    offer["url"] = "https://www.avito.ru" + item["uri_mweb"]
#    offer["offer_id"] = item["id"]

#    price = ''.join(item['price'].replace(' ₽ в месяц', '').split())
#    title = item['title'].split(', ')
#    area = float(title[1].replace(' м²', '').replace(',', '.'))
#    print(f'title[1] = {str(title[1])}')
#    rooms = title[0]
#     floor_info = title[2].replace(' эт.', '').split('/')
#     floor = floor_info[0]
#     total_floor = floor_info[-1]

    # timestamp = datetime.fromtimestamp(item['time'])
    # timestamp = datetime.strftime(timestamp, '%Y-%m-%d %H:%M:%S')
    # offer["date"] = timestamp

#    offer["price"] = price
#    offer["address"] = f"{item['location']}, {item['address']}"
#    offer["area"] = area
#    offer["rooms"] = rooms
#    offer["floor"] = floor
#    offer["total_floor"] = total_floor

    print(f'offer {offer}')
    return offer


def get_offers(data):
    #ok print(f'DATA =++++++++++++++++ {data}')
    items = data["result"]["items"]
    #ok print(f'items =++++++++++++++++ {items}')
    for item in items:
        if "item" in item["type"]:
            offer = get_offer(item["value"])
            print(f'Offer to DB = {offer}')
            check_database(offer)


def get_json():
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

    params = {
        'key': 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir',
        'categoryId': 24,
        'params[30]': 4969,
        'params[201]': 1060,
        'locationId': 107620,
        'params[504]': '5256',
        'searchRadius': 100,
        'priceMin': 50000,
        'priceMax': 5000000,
        'params[110275]': 426645,
        'sort': 'priceDesc',
        'withImagesOnly': 'true',
        'lastStamp': 1660975970,
        'display': 'list',
        'limit': 30,
    }

    session = requests.session()
    adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
    session.mount("https://", adapter)
    headers['cookie'] = cookie
    session.headers.update(headers)  # Сохраняем заголовки в сессию
    session.get('https://m.avito.ru/') #, proxies=proxiess)
    url_api_9 = 'https://m.avito.ru/api/9/items'
    #url = url_api_9

    resp = session.get(url_api_9, params=params)#, proxies = proxiess)

    try:
        res = resp.json()
        #response = session.request('GET', url, headers=headers, params=params)
        #r = session.request('GET', 'https://www.avito.ru')
        print(res)
    except Exception as exception:
        print(exception)

    #response = requests.get(url=url, headers=headers, params=params)
    data = res #response.json()

    return data


def main():
    data = get_json()
    print(data)
    get_offers(data)


if __name__ == '__main__':
    main()
