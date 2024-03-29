import httpx
import asyncio
import ssl
from twocaptcha import TwoCaptcha
#pip install TwoCaptcha
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
    ssl_context = httpx.create_ssl_context()
    ssl_context.set_alpn_protocols(["h2"])
    CIPHERS = 'ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES'
    ssl_context.set_ciphers(CIPHERS)

    async with httpx.AsyncClient(headers=headers, verify=ssl_context) as client:
        response = await client.get(url, params=params)
        if response.status_code == 200:
            try:
                return response.json()
            except json.JSONDecodeError as e:
                print(f"Ошибка при декодировании JSON: {e}")
        else:
            print(f"Ошибка сервера: {response.status_code}")


async def main():
    url_api_10 = 'https://m.avito.ru/api/10/items'
    url_api_web1 = 'https://www.avito.ru/web/1/main/items'
    url = url_api_10

    response = await make_request(url, params=params)

    if isinstance(response, dict):
        captcha_image_url = response.get('link')
        if captcha_image_url:
            captcha_text = await solve_captcha(captcha_image_url)

            params['captchaSolution'] = captcha_text

            response = await make_request(url, params=params)
            if isinstance(response, dict):
                print(response)
            else:
                print("Ошибка: получен неверный тип данных в ответе.")
        else:
            print("Ошибка: не удалось получить URL изображения капчи.")
    else:
        print("Ошибка: получен неверный тип данных в ответе.")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
