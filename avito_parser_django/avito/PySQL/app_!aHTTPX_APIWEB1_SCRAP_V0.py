import json
import sys
import time
# from random import randint
import random
import ssl
import httpx

#{'category': {
# 'id': 14, 'slug': 'mototsikly_i_mototehnika'
# },
# 'id': 3248339949,
# 'images': [{'208x156': 'https://10.img.avito.st/image/1/1.Og_RUba1lubH8SzmqXluT_7zlOZv-jTn3_CU5A.RQl6ncnwW1ro0lddcOgMV-tjzUYbsjVjYH7ZOPQ3J20', '236x177': 'https://10.img.avito.st/image/1/1.Og_RUba1lua_8XbmqXluT_7zlOZv-kznhfCU5A.BN1EoQNaMz7sTYbccheyvRM_tJi9efJNoGkk-9aTfhI', '240x180': 'https://10.img.avito.st/image/1/1.Og_RUba1luaH8XzmqXluT_7zlOZv-nTnj_CU5A.1aoxet7uK2oNvZ7ZEUjpJZCbBw0SwDyJxJMPFsEt4XE', '416x312': 'https://10.img.avito.st/image/1/1.Og_RUba1luan9GTgqXluT_7zlOZv-lTil_aU5A.xkKgHoYJdURupwyHAQC4NqieRyKnpcYMWKVbzb3RNkM', '432x324': 'https://10.img.avito.st/image/1/1.Og_RUba1luaH9BzhqXluT_7zlOZv-nTi7_eU5A.8Z4j6Tfc2Ref2XQlTdLvHNBkbvTvzP1NYU_aZSrLCwI', '472x354': 'https://10.img.avito.st/image/1/1.Og_RUba1lubX9VDhqXluT_7zlOZv-iTjo_eU5A.0QE5fsu2zrVsHIx8lgiyX0TtNRcIhURuRTwpLXEEdwM', '864x648': 'https://10.img.avito.st/image/1/1.Og_RUba1luan_wTuqXluT_7zlOZv-lTp9_iU5A.iXsmE769VDh9gpga71sVU_lItH-n8WSSSwxCVbB_YbE'}, {'208x156': 'https://70.img.avito.st/image/1/1._dhH0ba1UTFRcesxMf6pmGhzUzH5evMwSXBTMw.-c76_tvcF5sJ22JKlEKoXOJqoJBImHf5FBHBmOoVruQ', '236x177': 'https://70.img.avito.st/image/1/1._dhH0ba1UTEpcbExMf6pmGhzUzH5eoswE3BTMw.oluYkiKscjpl1cdPavDzQuUgjCzmN1805kD1kz0hvao', '240x180': 'https://70.img.avito.st/image/1/1._dhH0ba1UTERcbsxMf6pmGhzUzH5erMwGXBTMw.DxOwQMsX-pON03r63jbWW_dYLpk44wWYWZ3y5iS9XH0', '416x312': 'https://70.img.avito.st/image/1/1._dhH0ba1UTExdKM3Mf6pmGhzUzH5epM1AXZTMw.A3b8okGOQu8C6GXaipOvy4I_mCF4_ZrvF1x-q81sKQA', '432x324': 'https://70.img.avito.st/image/1/1._dhH0ba1UTERdNs2Mf6pmGhzUzH5erM1eXdTMw.DN0kzDtpnlhjw0KHv1PNKziXYxCcqSqLDoC9rMBBH7o', '472x354': 'https://70.img.avito.st/image/1/1._dhH0ba1UTFBdZc2Mf6pmGhzUzH5euM0NXdTMw.hHyg-lEn1iwA3R2gD_-nDB3rfgQcIREahd6HIXLa3no', '864x648': 'https://70.img.avito.st/image/1/1._dhH0ba1UTExf8M5Mf6pmGhzUzH5epM-YXhTMw.q7PZY8kJuali9awYD4qUHLRHFU_ITf03lhUV5YO-p1o'}, {'208x156': 'https://80.img.avito.st/image/1/1.-oxUR7a1VmVC5-xlLGiuzHvlVGXq7PRkWuZUZw.yhQCkZoqnLqGur72ic2FkX4egzPv4cwP1-RTEdamEko', '236x177': 'https://80.img.avito.st/image/1/1.-oxUR7a1VmU657ZlLGiuzHvlVGXq7IxkAOZUZw.sNuWzDgL1mxMGtPEXuoBxs74GJtzyKlrC5Mxxa4w4Pk', '240x180': 'https://80.img.avito.st/image/1/1.-oxUR7a1VmUC57xlLGiuzHvlVGXq7LRkCuZUZw.IJVKTfOmEAzRLn-MuRavQ_jnsxDMH816MH-JgVgvGZM', '416x312': 'https://80.img.avito.st/image/1/1.-oxUR7a1VmUi4qRjLGiuzHvlVGXq7JRhEuBUZw.DdWiYRnr6D4G6Jw3b70g4C6bd-stO7da2KP8FXIBVo8', '432x324': 'https://80.img.avito.st/image/1/1.-oxUR7a1VmUC4txiLGiuzHvlVGXq7LRhauFUZw.pWihCjMXMW2upy3i1KFek-kD2tnvr6GaLU0FOp4dzpY', '472x354': 'https://80.img.avito.st/image/1/1.-oxUR7a1VmVS45BiLGiuzHvlVGXq7ORgJuFUZw.kTjx8HpHtyaAS83sIKrdHMTt17KS2o9I9pb8RjHVzFk', '864x648': 'https://80.img.avito.st/image/1/1.-oxUR7a1VmUi6cRtLGiuzHvlVGXq7JRqcu5UZw.j1wpHI8YASHf9QgXWiN7mJLEiGCMyBLesLMgxog5mfE'}, {'208x156': 'https://10.img.avito.st/image/1/1.PFKvX7a1kLu5_yq723doEoD9krsR9DK6of6SuQ.FD2uit4bNg_sBSaG6p3MVSBG6F5Ta5Io5Znvoq_2Zt0', '236x177': 'https://10.img.avito.st/image/1/1.PFKvX7a1kLvB_3C723doEoD9krsR9Eq6-_6SuQ.rqAR5JrkDLt-K5P3Zouw06SE812plpCI9uY8Hnk9SVU', '240x180': 'https://10.img.avito.st/image/1/1.PFKvX7a1kLv5_3q723doEoD9krsR9HK68f6SuQ.WgssKWzZA1jmiHXWTkxdaBaXyYFEdbupnkMBchsO-qg', '416x312': 'https://10.img.avito.st/image/1/1.PFKvX7a1kLvZ-mK923doEoD9krsR9FK_6fiSuQ.dtnbjtw6Vf3yEiip4blm3vOpseyXtyhwmQqVFEbQot0', '432x324': 'https://10.img.avito.st/image/1/1.PFKvX7a1kLv5-hq823doEoD9krsR9HK_kfmSuQ.0AKfBiFIEPCA4MITtQjtUPoHEVP_-khGG4GrA6lIMV4', '472x354': 'https://10.img.avito.st/image/1/1.PFKvX7a1kLup-1a823doEoD9krsR9CK-3fmSuQ.LdyWnXStnY-5JGJQ11HtFEElPyCct9vprFpqQb_GQlQ', '864x648': 'https://10.img.avito.st/image/1/1.PFKvX7a1kLvZ8QKz23doEoD9krsR9FK0ifaSuQ.L0GpR8Ga_3awwemn4bwYr4jSt_IhwXFbgTt6fTxXS9M'}, {'208x156': 'https://10.img.avito.st/image/1/1.mciJtLa1NSGfFI8ht5rNiKYWNyE3H5cghxU3Iw.MddFfs7ZSiwNIdXIa3MaCU5FEJPvd4AqfyWdK_tXvR0', '236x177': 'https://10.img.avito.st/image/1/1.mciJtLa1NSHnFNUht5rNiKYWNyE3H-8g3RU3Iw.scOr4exgz-wMWY2i-bh1vJn5YrGuySA7R2scRTuvMAI', '240x180': 'https://10.img.avito.st/image/1/1.mciJtLa1NSHfFN8ht5rNiKYWNyE3H9cg1xU3Iw.5XdsCq71Ii809_R6dTkKpgk7jXYuf5bTcaO044vdIY4', '416x312': 'https://10.img.avito.st/image/1/1.mciJtLa1NSH_Eccnt5rNiKYWNyE3H_clzxM3Iw.CmGfdVylt3_v50W7zGcIZbsbXiHmDorF54WhargLTNk', '432x324': 'https://10.img.avito.st/image/1/1.mciJtLa1NSHfEb8mt5rNiKYWNyE3H9cltxI3Iw.SPBoeyYiskGhSWhCQT0iUsTDezS8yHTXsoYMn5G7HE4', '472x354': 'https://10.img.avito.st/image/1/1.mciJtLa1NSGPEPMmt5rNiKYWNyE3H4ck-xI3Iw.X_-0Uh80mlbXQ45K6gIDhPyfvkJCwFsfFk6sYso2dT4', '864x648': 'https://10.img.avito.st/image/1/1.mciJtLa1NSH_Gqcpt5rNiKYWNyE3H_curx03Iw.VJIQOV6LtWYtGcHfdu3oujTNtKp8HfmpOuLPGRamBE0'}, {'208x156': 'https://90.img.avito.st/image/1/1.7RrEkLa1QfPSMPvzkr-5WusyQ_N6O-PyyjFD8Q.a0D6EhQZ1tLGuYCFXb7n9JKSsnVDkRQ9BSTAjSKLNY8', '236x177': 'https://90.img.avito.st/image/1/1.7RrEkLa1QfOqMKHzkr-5WusyQ_N6O5vykDFD8Q.hC0vdCeEcmMWhi1dqt_sHTem4Q3S1aCLqivmLC_xjY0', '240x180': 'https://90.img.avito.st/image/1/1.7RrEkLa1QfOSMKvzkr-5WusyQ_N6O6PymjFD8Q.yK3_loAFtz7qVeEFdEMAcm1E0rYcz_wmxLjA-uUat8w', '416x312': 'https://90.img.avito.st/image/1/1.7RrEkLa1QfOyNbP1kr-5WusyQ_N6O4P3gjdD8Q.MGiPHerfgBPxyT6Bq5a5r29-ar5Lfhz7pehRxD6yWAc', '432x324': 'https://90.img.avito.st/image/1/1.7RrEkLa1QfOSNcv0kr-5WusyQ_N6O6P3-jZD8Q.IHWXD9AYXTCkDBse64VKkTtt0mHZfE24hHTUaj-v9GI', '472x354': 'https://90.img.avito.st/image/1/1.7RrEkLa1QfPCNIf0kr-5WusyQ_N6O_P2tjZD8Q.zqssbhpYzPb5LEHHw73C_SVfDWZucnJRhIN0tn2G5PA', '864x648': 'https://90.img.avito.st/image/1/1.7RrEkLa1QfOyPtP7kr-5WusyQ_N6O4P84jlD8Q.tKtKzq5BXAqB2NIH5GqxYuM8R52Fk_wQjrWGXSUFS54'}, {'208x156': 'https://60.img.avito.st/image/1/1.qciJtLa1BSGfFL8h15r9iKYWByE3H6cghxUHIw.XUkco9HPVF-Ju6W0QsQy6KxrRMK8Ez-wMhB_AtGJiI0', '236x177': 'https://60.img.avito.st/image/1/1.qciJtLa1BSHnFOUh15r9iKYWByE3H98g3RUHIw.n3rlkptmCF1bt85XXQnPplyNXGpLzPlbmWH3mjZN59k', '240x180': 'https://60.img.avito.st/image/1/1.qciJtLa1BSHfFO8h15r9iKYWByE3H-cg1xUHIw.gxOyBm_UMXq9grzpsKcsz2lH3lvr0w_B7sPu3AkDQP8', '416x312': 'https://60.img.avito.st/image/1/1.qciJtLa1BSH_Efcn15r9iKYWByE3H8clzxMHIw.VklVyqEh-l2lFP60Sa9_N3PvUb99UR26bwjw43gKCUk', '432x324': 'https://60.img.avito.st/image/1/1.qciJtLa1BSHfEY8m15r9iKYWByE3H-cltxIHIw.AzmUbiTNQljW2xxdtiqrvPZErsBU11pv-8tTd_X0KAU', '472x354': 'https://60.img.avito.st/image/1/1.qciJtLa1BSGPEMMm15r9iKYWByE3H7ck-xIHIw.KNo-sJXkR64GZwN1DhD0A85nhLj0yQMHYKwuE82cAQs', '864x648': 'https://60.img.avito.st/image/1/1.qciJtLa1BSH_Gpcp15r9iKYWByE3H8curx0HIw.C-SvoNEow_pR7bJBdwDmAdVDeYUkCYOPHeNabKCxDjQ'}],
# 'imagesAlt': 'Питбайк mikilon MZK 125 pitbike (2021)',
# 'imagesCount': 7,
# 'location': {'id': 641780, 'name': 'Новосибирск, Октябрьская', 'namePrepositional': 'Новосибирске'},
# 'locationId': 641780,
# 'priceDetailed': {'postfix': '', 'string': '43\xa0600', 'value': 43600, 'valueOld': '', 'wasLowered': False},
# 'sortTimeStamp': 1689408054,
# 'title': 'Питбайк mikilon MZK 125 pitbike (2021)',
# 'urlPath': '/novosibirsk/mototsikly_i_mototehnika/pitbayk_mikilon_mzk_125_pitbike_2021_3248339949'}

# ЕСЛИ БЛОКИРУЕТ IP ВЫЗЫВАТЬ НЕСКОЛЬКО РАЗ
key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'
cookie = "__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=ef757cc130c5cd228be88e869369c654.1610912291"

#ssl_context = ssl.create_default_context()
#ssl_context.set_ciphers('ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES')
ssl_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)#+PROTOCOL_TLS_CLIENT) #PROTOCOL_TLS)#
ssl_context = httpx.create_ssl_context()
ssl_context.set_alpn_protocols(["h2"])
ssl_context.set_ciphers('ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM:DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES')

search = 'suzuki+gsx-r'  # Строка поиска на сайте и ниже параметры выбора города, радиуса разброса цены и т.п.
categoryId = '14'
locationId = 641780  # Новосибирск
searchRadius = 200
priceMin = 100000
priceMax = 200000
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

if cookie:
    headers['cookie'] = cookie

url_api_10 = 'https://m.avito.ru/api/10/items'
url_api_web1 = 'https://www.avito.ru/web/1/main/items'
url = url_api_web1

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
cicle_stop = True
cikle = 0
items = []
res = None
##############################

def random_sleep(min_sleep=1, max_sleep=5):
    sleep_time = random.uniform(min_sleep, max_sleep)
    time.sleep(sleep_time)


while cicle_stop:
    cikle += 1
    params['page'] = cikle
    response = httpx.get(url, params=params, verify=ssl_context)

    try:
        res = response.json()
        print('TRUETRUETRUETRUETRUETRUETRUETRUETRUETRUETRUETRUETRUETRUE')
#        print(res['status'])
    except json.decoder.JSONDecodeError:
        except_error(res)

    res_stat = response.status_code

#    print(response.text) #ДАЛЬШЕ ИДЕТ С ОШИБКАМИ DNS
#    with httpx.Client(headers=headers, verify=ssl_context) as client:
    if True:
        #response = client.get(url, params=params)
#        response = httpx.get(url, params=params, verify=ssl_context)
#        res_stat = response.status_code
        print(f"Статус выполнения запроса. Код статуса: {res_stat}")

        try:
            response.raise_for_status()
            res = response.json()
            print(response.url)
            print("resresresresresresresresresresresresresresresresresresresresresres")
            #print(res)
        except (httpx.HTTPError, json.JSONDecodeError) as e:
            print(f"Ошибка при выполнении запроса {cikle}: {e}")
            sys.exit(1)

        #if res.get('status') != 'ok':
        if res_stat != 200:
            print(f"Запрос {cikle} Ошибка сервера: {res.get('status')} __ {res['result']}")
            sys.exit(1)
        else:
       #     items_page = min(len(response['items']), params['limit'] - 1)
       #     lastStamp = response['result']['lastStamp']
            print("items_page")


            for item in res['items']:
                items.append(item)
                print(item)
                ad_id = str(item['id'])
                # val = item['value']
                # print(f'val  {val}')
                #random_sleep(1, 3)

            #if items_page < params['limit'] - 1:
                cicle_stop = False
# print(f'!!!!! ПОЛУЧИЛИ ИТЕМС') # {items}')
# index = 1
# for i in items: # Теперь идем по ябъявлениям:
#     ad_id = str(i['value']['id'])
#     val = i['value']
#     print(f'val  {val}')
#     category = val['category']
#     print(f'category  {category}')
#     time = val['time']
#     print(f'time  {time}')
#     title = val['title']
#     print(f'title  {title}')
#     images = ''
#     price = val['price']
#     print(f'price  {price}')
#     address = val['address']
#     print(f'address  {address}')
#     coords = val['coords']
#     print(f'coords  {coords}')
#     uri = val['uri']
#     print(f'uri  {uri}')
#     uri_mweb = val['uri_mweb']
#     print(f'uri_mweb  {uri_mweb}')
