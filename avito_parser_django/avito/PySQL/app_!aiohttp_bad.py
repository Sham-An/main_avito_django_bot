import aiohttp
import asyncio
import ssl
import sys

sys.setrecursionlimit(1500)

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

params = {
    'key': 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir',
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

async def make_request(url, params=None):
    #ssl_context = ssl.create_default_context()
    ssl_context.verify_mode = ssl.CERT_REQUIRED
    ssl_context.check_hostname = True
    ssl_context.load_default_certs()
##########################################
    ssl_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)  # +PROTOCOL_TLS_CLIENT) #PROTOCOL_TLS)#
    ssl_context = ssl.create_default_context()#create_ssl_context()
    ssl_context.set_alpn_protocols(["h2"])
    ssl_context.set_ciphers(
        'ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES')

    async with aiohttp.ClientSession(headers=headers, connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        async with session.get(url, params=params) as response:
            print(response.url)
            return await response.text()

async def main():
    url_api_10 = 'https://m.avito.ru/api/10/items'
    url_api_web1 = 'https://www.avito.ru/web/1/main/items'
    url = url_api_web1
    response = await make_request(url, params=params)
    print(response)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())



'''
import aiohttp
import asyncio

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

params = {
    'key': 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir',
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
#verify=ssl_context
async def make_request(url, params=None):
    async with aiohttp.ClientSession(headers=headers, connector=aiohttp.TCPConnector(ssl=True)) as session:
        async with session.get(url, params=params) as response:
            print(response.url)
            return await response.text()

async def main():
    url_api_10 = 'https://m.avito.ru/api/10/items'
    url_api_web1 = 'https://www.avito.ru/web/1/main/items'
    url = url_api_web1
    response = await make_request(url, params=params)
    print(response)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

'''