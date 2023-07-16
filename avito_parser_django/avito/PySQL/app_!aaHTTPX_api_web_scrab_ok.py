import httpx
import time
from random import randint
# import ssl
import ssl
import httpx
import certifi

# import requests

# URL для GET-запроса
# url = "https://www.example.com"
cookie = '__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=ef757cc130c5cd228be88e869369c654.1610912291; _ga=GA1.2.559434019.1610912292; _gid=GA1.2.381990959.1610912292; _fbp=fb.1.1610912292358.1831979940; u=2oiycodt.1oaavs8.dyu0a4x7fxw0; v=1610912321; buyer_laas_location=641780; buyer_location_id=641780; luri=novosibirsk; buyer_selected_search_radius4=0_general; buyer_local_priority_v2=0; sx=H4sIAAAAAAACAxXLQQqAIBAF0Lv8dYvRLEdvU0MIBU0iKCHePXr71zGfefd1W5RLYick2kSakiB2VETclpf85n19RJMSp4vJOSlM%2F2BMOBDNaigE9taM8QH0oydNVAAAAA%3D%3D; dfp_group=100; _ym_uid=1610912323905107257; _ym_d=1610912323; _ym_visorc_34241905=b; _ym_isad=2; _ym_visorc_419506=w; _ym_visorc_188382=w; __gads=ID=2cff056a4e50a953-22d0341a94b900a6:T=1610912323:S=ALNI_MZMbOe0285QjW7EVvsYtSa-RA_Vpg; f=5.8696cbce96d2947c36b4dd61b04726f1a816010d61a371dda816010d61a371dda816010d61a371dda816010d61a371ddbb0992c943830ce0bb0992c943830ce0bb0992c943830ce0a816010d61a371dd2668c76b1faaa358c08fe24d747f54dc0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b978e38434be2a23fac7b9c4258fe3658d831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013a20f3d16ad0b1c5462da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bdf0c77052689da50d2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab91e52da22a560f5503c77801b122405c48ab0bfc8423929a6d7a5083cc1669877def5708993e2ca678f1dc04f891d61e35b0929bad7c1ea5dec762b46b6afe81f200c638bc3d18ce60768b50dd5e12c30e37135e8f7c6b64dc9f90003c0354a346b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7acf8b817f3dc0c3f21c1eac53cc61955882da10fb74cac1eab2da10fb74cac1eab5e5aa47e7d07c0f95e1e792141febc9cb841da6c7dc79d0b'
# ssl_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)  # +PROTOCOL_TLS_CLIENT) #PROTOCOL_TLS)#
ssl_context = httpx.create_ssl_context()
ssl_context.set_alpn_protocols(["h2"])
CIPHERS = 'ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES'
ssl_context.set_ciphers(CIPHERS)
key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'  # ключ, с которым всё работает, не разбирался где его брать, но похоже он статичен, т.к. гуглится на различных форумах

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

search = 'suzuki+gsx-r'  # Строка поиска на сайте и ниже параметры выбора города, радиуса разброса цены и т.п.
categoryId = '14'
locationId = 641780  # Новосибирск
searchRadius = 200
priceMin = 100000
priceMax = 200000
sort = 'priceDesc'
withImagesOnly = 'true'  # Только с фото
limit_page = 50  # Количество объявлений на странице 50 максимум

params = {
    'key': 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir',
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

url_api_10 = 'https://m.avito.ru/api/10/items'
# https://www.avito.ru/web/1/main/items?forceLocation=False&locationId=653040&lastStamp=1683748131&limit=30&offset=89&categoryId=24
url_api_web1 = 'https://www.avito.ru/web/1/main/items'
url = url_api_web1
# headers['cookie'] = cookie
cicle_stop = True  # Переменная для остановки цикла
cikle = 0  # Переменная для перебора страниц с объявлениями
items = []  # Список, куда складываем объявления

# Создание экземпляра httpx.Client с настройками повторных запросов
with httpx.Client(verify=ssl_context) as client:
    response = client.get(url_api_10, params=params)
    # with httpx.Client() as client:
    #     response = client.get(url_api_10, params=params, verify=True) #verify=certifi.where() verify=ssl_context
    # response = httpx.get(url_api_web1, params=params, verify=ssl_context)

    if response.status_code != 200:
        # Если получен код ответа, указывающий на ошибку, повторяем запрос до выполнения заданного количества попыток
        retries = 3
        retry_count = 0
        while response.status_code != 200 and retry_count < retries:
            response = client.get(url)
            retry_count += 1
    print(response.url)
    print(response.text)


def ssl_test():
    # Создание SSL-контекста
    ssl_context = ssl.create_default_context()

    # Вывод информации о сертификате
    ssl_info = ssl_context.get_ca_certs()
    for cert in ssl_info:
        print(f"Subject: {cert['subject']}")
        print(f"Issuer: {cert['issuer']}")
        print(f"Expiry Date: {cert['notAfter']}")
        print()

    # Вывод информации о доверенных корневых сертификатах
    root_certs = ssl_context.get_ca_certs()
    for cert in root_certs:
        print(f"Subject: {cert['subject']}")
        print(f"Issuer: {cert['issuer']}")
        print(f"Expiry Date: {cert['notAfter']}")
        print()


def sert_avito_info():
    import ssl
    import socket

    def get_certificate_info(domain):
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                return cert

    # Пример использования для Avito
    cert_info = get_certificate_info("www.avito.ru")
    print('\n cert_info \n')
    print(cert_info)


# {'subject': ((('countryName', 'RU'),), (('stateOrProvinceName', 'Moscow'),),
# (('localityName', 'Moscow'),),
# (('organizationName', 'Limited Liability Company KEH eCommerce'),),
# (('commonName', '*.avito.ru'),)),
# 'issuer': ((('countryName', 'BE'),),
# (('organizationName', 'GlobalSign nv-sa'),),
# (('commonName', 'GlobalSign RSA OV SSL CA 2018'),)),
# 'version': 3, 'serialNumber': '7BE56C1A231671F89206BD3B',
# 'notBefore': 'Apr  6 13:03:05 2023 GMT',
# 'notAfter': 'May  7 13:03:04 2024 GMT',
# 'subjectAltName': (('DNS', '*.avito.ru'),
# ('DNS', 'avito.ru')), 'OCSP': ('http://ocsp.globalsign.com/gsrsaovsslca2018',),
# 'caIssuers': ('http://secure.globalsign.com/cacert/gsrsaovsslca2018.crt',),
# 'crlDistributionPoints': ('http://crl.globalsign.com/gsrsaovsslca2018.crl',)}


# if __name__ == '__main__':
#     sert_avito_info()
#     # ssl_test()

"""
Устанавливаете пакет свежих корневых сертификатов
pip install certifi
и используете их для валидации
import certifi

r = requests.get(url, verify=certifi.where())

Чтобы проверить корректность подключения сертификата, вы можете использовать следующий пример кода:

python
import ssl

# Создание SSL-контекста
ssl_context = ssl.create_default_context()

# Вывод информации о сертификате
ssl_info = ssl_context.get_ca_certs()
for cert in ssl_info:
    print(f"Subject: {cert['subject']}")
    print(f"Issuer: {cert['issuer']}")
    print(f"Expiry Date: {cert['expiry_date']}")
    print()

# Вывод информации о доверенных корневых сертификатах
root_certs = ssl.get_default_verify_paths().anchors
for cert in root_certs:
    print(f"Subject: {cert['subject']}")
    print(f"Issuer: {cert['issuer']}")
    print(f"Expiry Date: {cert['expiry_date']}")
    print()


Этот код создает SSL-контекст и выводит информацию о сертификатах, которые используются в этом контексте. Здесь вы можете проверить, что SSL-контекст содержит правильно установленные и актуальные корневые сертификаты и что он настроен правильно.

Если вы обнаружите ошибку или отсутствие корневого сертификата, вам нужно убедиться, что все необходимые корневые сертификаты установлены или обновлены в вашей системе. Если вы не можете получить актуальные корневые сертификаты, вы можете попробовать использовать функцию load_verify_locations() из модуля ssl для явного указания пути к корневым сертификатам.


/1/searchSubscription/new/byParams?description=%D0%9C%D0%BE%D1%82%D0%BE%D1%86%D0%B8%D0%BA%D0%BB%D1%8B+%D0%B8+%D0%BC%D0%BE%D1%82%D0%BE%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D0%BA%D0%B0%2C+%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA%2C+%D0%9E%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C+%D0%BD%D0%B0+%D0%BA%D0%B0%D1%80%D1%82%D0%B5%2C+suzuki%2Bgsx-r%2C+%D0%9C%D0%BE%D1%82%D0%BE%D1%86%D0%B8%D0%BA%D0%BB%D1%8B%2C+%D0%91%2F%D1%83%2C+%D0%A2%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE+%D1%81+%D1%84%D0%BE%D1%82%D0%BE%2C+%D0%A6%D0%B5%D0%BD%D0%B0+100%C2%A0000%C2%A0%E2%80%94%C2%A0200%C2%A0000%C2%A0%E2%82%BD\u0026filter%5BcategoryId%5D=14\u0026filter%5BlocationId%5D=641780\u0026filter%5Bparams%5D%5B110275%5D=426645\u0026filter%5Bparams%5D%5B30%5D=4969\u0026filter%5BpriceMax%5D=200000\u0026filter%5BpriceMin%5D=100000\u0026filter%5Bquery%5D=suzuki%2Bgsx-r\u0026filter%5BsearchRadius%5D=200\u0026filter%5BwithImagesOnly%5D=1\u0026pushFrequency=3\u0026pushFrequencyOptions%5B0%5D%5Bid%5D=1\u0026pushFrequencyOptions%5B0%5D%5Btitle%5D=%D0%A1%D1%80%D0%B0%D0%B7%D1%83\u0026pushFrequencyOptions%5B1%5D%5Bid%5D=2\u0026pushFrequencyOptions%5B1%5D%5Btitle%5D=%D0%A3%D1%82%D1%80%D0%BE%D0%BC\u0026pushFrequencyOptions%5B2%5D%5Bid%5D=3\u0026pushFrequencyOptions%5B2%5D%5Btitle%5D=%D0%92%D0%B5%D1%87%D0%B5%D1%80%D0%BE%D0%BC\u0026pushFrequencyOptions%5B3%5D%5Bid%5D=0\u0026pushFrequencyOptions%5B3%5D%5Btitle%5D=%D0%9D%D0%B5+%D0%BF%D1%80%D0%B8%D1%81%D1%8B%D0%BB%D0%B0%D1%82%D1%8C\u0026title=%D0%9F%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%BA%D0%B0+%D0%BD%D0%B0+%D0%BF%D0%BE%D0%B8%D1%81%D0%BA
"""
