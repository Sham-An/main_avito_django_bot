import httpx
import time
from random import randint
import ssl

class AvitoScraper:
    def __init__(self):
        self.ssl_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)
        self.ssl_context = httpx.create_ssl_context()
        self.ssl_context.set_alpn_protocols(["h2"])
        self.key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
        CIPHERS = 'ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES'
        self.ssl_context.set_ciphers(CIPHERS)

        url_api_10 = 'https://m.avito.ru/api/10/items'
        url_api_web1 = 'https://www.avito.ru/web/1/main/items'
        self.url = url_api_10


        self.headers = {
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

        self.params = {
            'key': self.key,
            'categoryId': 14,
            'params[30]': 4969,
            'locationId': 641780,
            'searchRadius': 200,
            'priceMin': 100000,
            'priceMax': 200000,
            'params[110275]': 426645,
            'sort': 'priceDesc',
            'withImagesOnly': 'true',
            'lastStamp': 1660975970,
            'display': 'list',
            'limit': 50,
            'query': 'suzuki+gsx-r',
        }


#        self.session = httpx.Client(http2=True, headers=self.headers, verify=ssl_context)
        #self.session = httpx.Client(http2=True, headers=self.headers, verify=True)
        self.session = httpx.get(self.url, params=self.params, headers=self.headers, verify=self.ssl_context)
        self.resp = httpx.get(self.url, params=self.params, verify=self.ssl_context)

        self.key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
        self.cookie = '__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=ef757cc130c5cd228be88e869369c654.1610912291; _ga=GA1.2.559434019.1610912292; _gid=GA1.2.381990959.1610912292; _fbp=fb.1.1610912292358.1831979940; u=2oiycodt.1oaavs8.dyu0a4x7fxw0; v=1610912321; buyer_laas_location=641780; buyer_location_id=641780; luri=novosibirsk; buyer_selected_search_radius4=0_general; buyer_local_priority_v2=0; sx=H4sIAAAAAAACAxXLQQqAIBAF0Lv8dYvRLEdvU0MIBU0iKCHePXr71zGfefd1W5RLYick2kSakiB2VETclpf85n19RJMSp4vJOSlM%2F2BMOBDNaigE9taM8QH0oydNVAAAAA%3D%3D; dfp_group=100; _ym_uid=1610912323905107257; _ym_d=1610912323; _ym_visorc_34241905=b; _ym_isad=2; _ym_visorc_419506=w; _ym_visorc_188382=w; __gads=ID=2cff056a4e50a953-22d0341a94b900a6:T=1610912323:S=ALNI_MZMbOe0285QjW7EVvsYtSa-RA_Vpg; f=5.8696cbce96d2947c36b4dd61b04726f1a816010d61a371dda816010d61a371dda816010d61a371dda816010d61a371ddbb0992c943830ce0bb0992c943830ce0bb0992c943830ce0a816010d61a371dd2668c76b1faaa358c08fe24d747f54dc0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b978e38434be2a23fac7b9c4258fe3658d831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013a20f3d16ad0b1c5462da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bdf0c77052689da50d2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab91e52da22a560f5503c77801b122405c48ab0bfc8423929a6d7a5083cc1669877def5708993e2ca678f1dc04f891d61e35b0929bad7c1ea5dec762b46b6afe81f200c638bc3d18ce60768b50dd5e12c30e37135e8f7c6b64dc9f90003c0354a346b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7acf8b817f3dc0c3f21c1eac53cc61955882da10fb74cac1eab2da10fb74cac1eab5e5aa47e7d07c0f95e1e792141febc9cb841da6c7dc79d0b'


    def get_with_cloudscraper(self):
        print(self.params)
        headers = self.headers
        params = self.params
        #response = self.session
        #response = self.session.get(self.url, params=params, headers=headers)
        #response = httpx.get(self.url, params=params, headers=headers)
        response = self.resp
        #response = httpx.get(url, params=params, verify=ssl_context)
        print(response.url)

        #https://www.avito.ru/web/1/main/items?key=af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir&categoryId=14&params%5B30%5D=4969&locationId=641780&searchRadius=200&priceMin=100000&priceMax=200000&params%5B110275%5D=426645&sort=priceDesc&withImagesOnly=true&lastStamp=1660975970&display=list&limit=50&query=suzuki%2Bgsx-r
        print('11111111111111111111111111111111111111111')
        print(response.text[:1000])
        return response.text

    def get_with_httpx(self):
        print('get_with_httpx get_with_httpx get_with_httpx get_with_httpx')
        print(self.params)
       #headers = self.headers
       #params = self.params
        response = self.session#.get(self.url, headers=headers, params=params)
        response = self.resp
        return response.text

    def close(self):
        self.session.close()
        self.resp.close()


# Пример использования класса AvitoScraper
scraper = AvitoScraper()
response_cloudscraper = scraper.get_with_cloudscraper()
print(response_cloudscraper[:100])
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
response_httpx = scraper.get_with_httpx()
print(response_httpx)

scraper.close()


#??????????????????????????????????????????????????????????????????????


# class AvitoScraper:
#     def __init__(self):
#         #ssl_context = ssl.create_default_context()
#         #ssl_context = httpx.create_ssl_context()
#         ssl_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)  # +PROTOCOL_TLS_CLIENT) #PROTOCOL_TLS)#
#         #ssl_context = httpx.create_ssl_context()
#         ssl_context.set_alpn_protocols(["h2"])
#
#         CIPHERS = 'ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES'
#         ssl_context.set_ciphers(CIPHERS)
#         url_api_10 = 'https://m.avito.ru/api/10/items'
#         url_api_web1 = 'https://www.avito.ru/web/1/main/items'
#         self.url = url_api_web1
#
#         self.headers = {
#             'Host': 'm.avito.ru',
#             'pragma': 'no-cache',
#             'cache-control': 'no-cache',
#             'upgrade-insecure-requests': '1',
#             'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
#             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#             'sec-fetch-site': 'none',
#             'sec-fetch-mode': 'navigate',
#             'sec-fetch-user': '?1',
#             'sec-fetch-dest': 'document',
#             'accept-language': 'ru-RU,ru;q=0.9',
#         }
#
#         self.session = httpx.Client(http2=True, headers=self.headers, verify=ssl_context)
#         self.key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
#         self.cookie = "__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=ef757cc130c5cd228be88e869369c654.1610912291; _ga=GA1.2.559434019.1610912292;"
#
#         self.params = {
#             'key': self.key,
#             'categoryId': 14,
#             'params[30]': 4969,
#             'locationId': 641780,
#             'searchRadius': 200,
#             'priceMin': 100000,
#             'priceMax': 200000,
#             'params[110275]': 426645,
#             'sort': 'priceDesc',
#             'withImagesOnly': 'true',
#             'lastStamp': 1660975970,
#             'display': 'list',
#             'limit': 50,
#             'query': 'suzuki+gsx-r',
#         }
#
#     def get_with_cloudscraper(self):
#         headers = {
#             'cookie': self.cookie,
#             'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#         }
#         response = self.session.get(self.url, headers=headers)
#         return response.text
#
#     def get_with_httpx(self):
#         headers = {
#             'cookie': self.cookie,
#             'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#         }
#         response = self.session.get(self.url, headers=headers, params=self.params)
#         return response.text
#
#     def close(self):
#         self.session.close()
#
#
# # Пример использования класса AvitoScraper
# scraper = AvitoScraper()
# response_cloudscraper = scraper.get_with_cloudscraper()
# print(response_cloudscraper)
# print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
# response_httpx = scraper.get_with_httpx()
# print(response_httpx)
#
# scraper.close()

"""
'__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=ef757cc130c5cd228be88e869369c654.1610912291; _ga=GA1.2.559434019.1610912292; _gid=GA1.2.381990959.1610912292; _fbp=fb.1.1610912292358.1831979940; u=2oiycodt.1oaavs8.dyu0a4x7fxw0; v=1610912321; buyer_laas_location=641780; buyer_location_id=641780; luri=novosibirsk; buyer_selected_search_radius4=0_general; buyer_local_priority_v2=0; sx=H4sIAAAAAAACAxXLQQqAIBAF0Lv8dYvRLEdvU0MIBU0iKCHePXr71zGfefd1W5RLYick2kSakiB2VETclpf85n19RJMSp4vJOSlM%2F2BMOBDNaigE9taM8QH0oydNVAAAAA%3D%3D; dfp_group=100; _ym_uid=1610912323905107257; _ym_d=1610912323; _ym_visorc_34241905=b; _ym_isad=2; _ym_visorc_419506=w; _ym_visorc_188382=w; __gads=ID=2cff056a4e50a953-22d0341a94b900a6:T=1610912323:S=ALNI_MZMbOe0285QjW7EVvsYtSa-RA_Vpg; f=5.8696cbce96d2947c36b4dd61b04726f1a816010d61a371dda816010d61a371dda816010d61a371dda816010d61a371ddbb0992c943830ce0bb0992c943830ce0bb0992c943830ce0a816010d61a371dd2668c76b1faaa358c08fe24d747f54dc0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b978e38434be2a23fac7b9c4258fe3658d831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013a20f3d16ad0b1c5462da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bdf0c77052689da50d2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab91e52da22a560f5503c77801b122405c48ab0bfc8423929a6d7a5083cc1669877def5708993e2ca678f1dc04f891d61e35b0929bad7c1ea5dec762b46b6afe81f200c638bc3d18ce60768b50dd5e12c30e37135e8f7c6b64dc9f90003c0354a346b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7acf8b817f3dc0c3f21c1eac53cc61955882da10fb74cac1eab2da10fb74cac1eab5e5aa47e7d07c0f95e1e792141febc9cb841da6c7dc79d0b'

class AvitoScraper:
    def __init__(self):
        ssl_context = ssl.create_default_context()
        ssl_context.set_alpn_protocols(["h2"])
        CIPHERS = 'ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES'
        ssl_context.set_ciphers(CIPHERS)
        url_api_10 = 'https://m.avito.ru/api/10/items'
        # https://www.avito.ru/web/1/main/items?forceLocation=False&locationId=653040&lastStamp=1683748131&limit=30&offset=89&categoryId=24
        url_api_web1 = 'https://www.avito.ru/web/1/main/items'
        self.url = url_api_web1
        self.headers = {
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

        self.session = httpx.Client(http2=True, headers=self.headers, verify=ssl_context)
        self.key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
        self.cookie = '__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=ef757cc130c5cd228be88e869369c654.1610912291; _ga=GA1.2.559434019.1610912292; _gid=GA1.2.381990959.1610912292; _fbp=fb.1.1610912292358.1831979940; u=2oiycodt.1oaavs8.dyu0a4x7fxw0; v=1610912321; buyer_laas_location=641780; buyer_location_id=641780; luri=novosibirsk; buyer_selected_search_radius4=0_general; buyer_local_priority_v2=0; sx=H4sIAAAAAAACAxXLQQqAIBAF0Lv8dYvRLEdvU0MIBU0iKCHePXr71zGfefd1W5RLYick2kSakiB2VETclpf85n19RJMSp4vJOSlM%2F2BMOBDNaigE9taM8QH0oydNVAAAAA%3D%3D; dfp_group=100; _ym_uid=1610912323905107257; _ym_d=1610912323; _ym_visorc_34241905=b; _ym_isad=2; _ym_visorc_419506=w; _ym_visorc_188382=w; __gads=ID=2cff056a4e50a953-22d0341a94b900a6:T=1610912323:S=ALNI_MZMbOe0285QjW7EVvsYtSa-RA_Vpg; f=5.8696cbce96d2947c36b4dd61b04726f1a816010d61a371dda816010d61a371dda816010d61a371dda816010d61a371ddbb0992c943830ce0bb0992c943830ce0bb0992c943830ce0a816010d61a371dd2668c76b1faaa358c08fe24d747f54dc0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b978e38434be2a23fac7b9c4258fe3658d831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013a20f3d16ad0b1c5462da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bdf0c77052689da50d2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab91e52da22a560f5503c77801b122405c48ab0bfc8423929a6d7a5083cc1669877def5708993e2ca678f1dc04f891d61e35b0929bad7c1ea5dec762b46b6afe81f200c638bc3d18ce60768b50dd5e12c30e37135e8f7c6b64dc9f90003c0354a346b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7acf8b817f3dc0c3f21c1eac53cc61955882da10fb74cac1eab2da10fb74cac1eab5e5aa47e7d07c0f95e1e792141febc9cb841da6c7dc79d0b'
        self.params = {
            'key': self.key,
            'categoryId': 14,
            'params[30]': 4969,
            'locationId': 641780,
            'searchRadius': 200,
            'priceMin': 100000,
            'priceMax': 200000,
            'params[110275]': 426645,
            'sort': 'priceDesc',
            'withImagesOnly': 'true',
            'lastStamp': 1660975970,
            'display': 'list',
            'limit': 50,
            'query': 'suzuki+gsx-r',
        }

    def get_with_cloudscraper(self):
        url_api_10 = 'https://m.avito.ru/api/10/items'
        # https://www.avito.ru/web/1/main/items?forceLocation=False&locationId=653040&lastStamp=1683748131&limit=30&offset=89&categoryId=24
        url_api_web1 = 'https://www.avito.ru/web/1/main/items'
        url = url_api_web1

        headers = {
            'cookie': self.cookie,
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }
        response = self.session.get(url, headers=headers)
        return response.text

    def get_with_httpx(self):
        params['key'] = self.key
        headers = {
            'cookie': self.cookie,
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }
        response = self.session.get(url, headers=headers, params=params)
        return response.text

    def close(self):
        self.session.close()

    # Пример использования класса AvitoScraper
scraper = AvitoScraper()
response_cloudscraper = scraper.get_with_cloudscraper()
print(response_cloudscraper)

response_httpx = scraper.get_with_httpx()
print(response_httpx)

scraper.close()

"""


'''
class AvitoScraper:
    def __init__(self):
        ssl_context = ssl.create_default_context()
        ssl_context.set_alpn_protocols(["h2"])
        CIPHERS = 'ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES'
        ssl_context.set_ciphers(CIPHERS)
        self.headers = {
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

        self.session = httpx.Client(http2=True, headers=self.headers, ssl=ssl_context)
        self.key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
        self.cookie = '__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=ef757cc130c5cd228be88e869369c654.1610912291; _ga=GA1.2.559434019.1610912292; _gid=GA1.2.381990959.1610912292; _fbp=fb.1.1610912292358.1831979940; u=2oiycodt.1oaavs8.dyu0a4x7fxw0; v=1610912321; buyer_laas_location=641780; buyer_location_id=641780; luri=novosibirsk; buyer_selected_search_radius4=0_general; buyer_local_priority_v2=0; sx=H4sIAAAAAAACAxXLQQqAIBAF0Lv8dYvRLEdvU0MIBU0iKCHePXr71zGfefd1W5RLYick2kSakiB2VETclpf85n19RJMSp4vJOSlM%2F2BMOBDNaigE9taM8QH0oydNVAAAAA%3D%3D; dfp_group=100; _ym_uid=1610912323905107257; _ym_d=1610912323; _ym_visorc_34241905=b; _ym_isad=2; _ym_visorc_419506=w; _ym_visorc_188382=w; __gads=ID=2cff056a4e50a953-22d0341a94b900a6:T=1610912323:S=ALNI_MZMbOe0285QjW7EVvsYtSa-RA_Vpg; f=5.8696cbce96d2947c36b4dd61b04726f1a816010d61a371dda816010d61a371dda816010d61a371dda816010d61a371ddbb0992c943830ce0bb0992c943830ce0bb0992c943830ce0a816010d61a371dd2668c76b1faaa358c08fe24d747f54dc0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b978e38434be2a23fac7b9c4258fe3658d831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013a20f3d16ad0b1c5462da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bdf0c77052689da50d2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab91e52da22a560f5503c77801b122405c48ab0bfc8423929a6d7a5083cc1669877def5708993e2ca678f1dc04f891d61e35b0929bad7c1ea5dec762b46b6afe81f200c638bc3d18ce60768b50dd5e12c30e37135e8f7c6b64dc9f90003c0354a346b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7acf8b817f3dc0c3f21c1eac53cc61955882da10fb74cac1eab2da10fb74cac1eab5e5aa47e7d07c0f95e1e792141febc9cb841da6c7dc79d0b'

    def get_with_cloudscraper(self):
        headers = {
            'cookie': self.cookie,
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }
        response = self.session.get(url, headers=headers)
        return response.text

    def get_with_httpx(self):
        params['key'] = self.key
        headers = {
            'cookie': self.cookie,
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }
        response = self.session.get(url, headers=headers, params=params)
        return response.text

        def close(self):
            self.session.close()

# Пример использования класса AvitoScraper
scraper = AvitoScraper()
response_cloudscraper = scraper.get_with_cloudscraper()
print(response_cloudscraper)

response_httpx = scraper.get_with_httpx()
print(response_httpx)

scraper.close()

'''