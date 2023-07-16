import json
import sys
import time
# from random import randint
import random
import ssl
import httpx

#id=3182603230
#GOVNO https://m.avito.ru/api/1/rmp/show/3182603230?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir

# ЕСЛИ БЛОКИРУЕТ IP ВЫЗЫВАТЬ НЕСКОЛЬКО РАЗ
key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
cookie = "__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=ef757cc130c5cd228be88e869369c654.1610912291"

# ssl_context = ssl.create_default_context()
# ssl_context.set_ciphers('ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES')
ssl_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)  # +PROTOCOL_TLS_CLIENT) #PROTOCOL_TLS)#
ssl_context = httpx.create_ssl_context()
ssl_context.set_alpn_protocols(["h2"])
ssl_context.set_ciphers(
    'ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES')

search = 'suzuki+gsx-r'  # Строка поиска на сайте и ниже параметры выбора города, радиуса разброса цены и т.п.
categoryId = '14'
locationId = 641780  # Новосибирск
searchRadius = 200
priceMin = 50000
priceMax = 100000
sort = 'priceDesc'
withImagesOnly = 'true'  # Только с фото
limit_page = 50  # Количество объявлений на странице 50 максимум

headers = {
    'Host': 'm.avito.ru',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'ru-RU,ru;q=0.9',
}

if cookie:  # Добавим куки, если есть внешние куки
    headers['cookie'] = cookie

url_api_10 = 'https://m.avito.ru/api/10/items'
url_api_web1 = 'https://www.avito.ru/web/1/main/items'
url = url_api_10

params = {
    'key': key,
    'categoryId': 14,
    'params[30]': 4969,
    'locationId': locationId,
    'searchRadius': searchRadius,
    'priceMin': priceMin,
    'priceMax': priceMax,
    'params[110275]': 426645,
    'sort': sort,
    'withImagesOnly': withImagesOnly,
    'lastStamp': 1660975970,
    'display': 'list',
    'limit': limit_page,
    'query': search,
}
cicle_stop = True  # Переменная для остановки цикла
cikle = 0  # Переменная для перебора страниц с объявлениями
items = []  # Список, куда складываем объявления
res = None


###########################################

def random_sleep(min_sleep=1, max_sleep=5):
    sleep_time = random.uniform(min_sleep, max_sleep)
    time.sleep(sleep_time)


while cicle_stop:
    cikle += 1  # Так как страницы начинаются с 1, то сразу же итерируем
    params['page'] = cikle
    res = httpx.get(url, params=params, verify=ssl_context)
    print(res.url)

    try:
        res = res.json()
    except json.decoder.JSONDecodeError:
        except_error(res)

    if res['status'] != 'ok':
        print(f'''result = {res['result']}''')
        print(f'''result = {res['status']}''')  # too-many-requests
        print(f'''result = NON''')
        sys.exit(1)
    if res['status'] == 'ok':
        items_page = int(len(res['result']['items']))
        lastStamp = int(res['result']['lastStamp'])
        print(f"res['status'] == 'ok': lastStamp {lastStamp}")
        print(res)

        if items_page > limit_page:  # проверка на "snippet"
            items_page = items_page - 1

        for item in res['result']['items']:
            if item['type'] == 'item':
                items.append(item)
        if items_page < limit_page:
            cicle_stop = False
print(f'!!!!! ПОЛУЧИЛИ ИТЕМС')  # {items}')
index = 1
for i in items:  # Теперь идем по ябъявлениям:
    ad_id = str(i['value']['id'])
    val = i['value']
    print(f'val  {val}')
    category = val['category']
    print(f'category  {category}')
    time = val['time']
    print(f'time  {time}')
    title = val['title']
    print(f'title  {title}')
    images = ''
    price = val['price']
    print(f'price  {price}')
    address = val['address']
    print(f'address  {address}')
    coords = val['coords']
    print(f'coords  {coords}')
    uri = val['uri']
    print(f'uri  {uri}')
    uri_mweb = val['uri_mweb']
    print(f'uri_mweb  {uri_mweb}')
