import json
import sqlite3
from contextlib import closing
from pprint import pprint
import realty

import ssl
import requests
# https://www.avito.ru/rostovskaya_oblast/mototsikly_i_mototehnika?cd=1&f=ASgCAgECAUXGmgwXeyJmcm9tIjoyMDAwLCJ0byI6NzAwMH0&q=скутер&s=1
#
from lxml import html
##########################################
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
from urllib3.util import ssl_
from fake_useragent import UserAgent
from urllib.parse import urlparse

ua = UserAgent(browsers=['edge', 'chrome'])
ua_str = ua.random
print(ua_str)
CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""

key = 'af0deccbgcgidddjgnvljitntccdduijhdinfgjgfjir'  # ключ, с которым всё работает, не разбирался где его брать, но похоже он статичен, т.к. гуглится на различных форумах
cookie = '__cfduid=da6b6b5b9f01fd022f219ed53ac3935791610912291; sessid=ef757cc130c5cd228be88e869369c654.1610912291; _ga=GA1.2.559434019.1610912292; _gid=GA1.2.381990959.1610912292; _fbp=fb.1.1610912292358.1831979940; u=2oiycodt.1oaavs8.dyu0a4x7fxw0; v=1610912321; buyer_laas_location=641780; buyer_location_id=641780; luri=novosibirsk; buyer_selected_search_radius4=0_general; buyer_local_priority_v2=0; sx=H4sIAAAAAAACAxXLQQqAIBAF0Lv8dYvRLEdvU0MIBU0iKCHePXr71zGfefd1W5RLYick2kSakiB2VETclpf85n19RJMSp4vJOSlM%2F2BMOBDNaigE9taM8QH0oydNVAAAAA%3D%3D; dfp_group=100; _ym_uid=1610912323905107257; _ym_d=1610912323; _ym_visorc_34241905=b; _ym_isad=2; _ym_visorc_419506=w; _ym_visorc_188382=w; __gads=ID=2cff056a4e50a953-22d0341a94b900a6:T=1610912323:S=ALNI_MZMbOe0285QjW7EVvsYtSa-RA_Vpg; f=5.8696cbce96d2947c36b4dd61b04726f1a816010d61a371dda816010d61a371dda816010d61a371dda816010d61a371ddbb0992c943830ce0bb0992c943830ce0bb0992c943830ce0a816010d61a371dd2668c76b1faaa358c08fe24d747f54dc0df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b978e38434be2a23fac7b9c4258fe3658d831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013a20f3d16ad0b1c5462da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bdf0c77052689da50d2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab91e52da22a560f5503c77801b122405c48ab0bfc8423929a6d7a5083cc1669877def5708993e2ca678f1dc04f891d61e35b0929bad7c1ea5dec762b46b6afe81f200c638bc3d18ce60768b50dd5e12c30e37135e8f7c6b64dc9f90003c0354a346b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7acf8b817f3dc0c3f21c1eac53cc61955882da10fb74cac1eab2da10fb74cac1eab5e5aa47e7d07c0f95e1e792141febc9cb841da6c7dc79d0b'


class TlsAdapter(HTTPAdapter):

    def __init__(self, ssl_options=0, **kwargs):
        self.ssl_options = ssl_options
        super(TlsAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
        self.poolmanager = PoolManager(*pool_args, ssl_context=ctx, **pool_kwargs)

def create_category_tab():
    '''Создаем базу категории и в неё загружаем словарь'''
    connection = sqlite3.connect('realty.db')
    cursor = connection.cursor()
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # Create Table if not exists categories (id Text, name Text, parentId Text, showMap Text)
    cursor.execute("""
        Create Table if not exists categories(
            id INTEGER PRIMARY KEY, 
            name Text,
            parentId Text, 
            showMap Text,
            url_path text,
            url_name text
            )     
    """)
    connection.commit()
    connection.close()

#####################################################
def check_category_path(id_dict, url_str, url_name_dict):
    url_name = url_name_dict[0]
    id = id_dict[0]

    # Узнать сколько строк было изменено через запрос cursor.rowcount
    # метод total_changes() показывает число строк было изменено во всей базе с момента подключения
    print(f' \n \n\n Function check_category_path {id} {url_str} {url_name}')
    id_find = id
    url_str = url_str

    reg_in = id_find
    reg1 = reg_in  + "%"
    reg2 = "%" + reg_in.lower() + "%"
    trupl_str = (reg1, reg2)
    # print(f'trupl_str {trupl_str}')

    list_str = []
    list_str.append(reg1)
    list_str.append(reg2)
    print(f"list_str {list_str}")

    dict_str = dict()
    values = [reg_in, reg_in]

    param_names = [f"reg{i + 1}" for i in range(len(values))]
    in_str = ", ".join(":" + p for p in param_names)  # print(",".join("Python")) >>>P,y,t,h,o,n
    params = dict(zip(param_names, values))
    # query_str_5 = f"""SELECT name, id FROM categories
    #                  WHERE id in ({in_str})"""
    #
    # sql = f"""
    # SELECT name, id FROM categories
    #          WHERE id in ({in_str}) ORDER BY id
    #          """
    sql = f"""UPDATE categories 
    SET url_path = ({url_str}) 
    WHERE id = ({in_str}) 
    """
    # ORDER BY id
    print(f'params {params} , in_str {in_str}, \n sql {sql} , url_str {url_str}')

    # query_str = """
    # SELECT name, id FROM categories WHERE id LIKE ? ORDER BY id
    #   """

    # query_str = f"""UPDATE categories
    #     SET url_name = ({url_str})
    #     WHERE id in ({in_str})
    #     """

    # OK!!!!!!
    query_str = f"""UPDATE categories 
        SET url_path = ?, url_name = ? 
        WHERE id = ?
        """

    # ORDER BY id
    query_str_3 = """
    SELECT name, id FROM categories WHERE (lower(id) LIKE ?) OR (lower(id) LIKE ?) ORDER BY id 
      """

    query_str_4 = """
    SELECT name, id FROM categories WHERE (lower(id) LIKE :reg1) OR (lower(id) LIKE :reg2) ORDER BY id 
      """

    with sqlite3.connect('realty.db', timeout=5) as connection:
        cursor = connection.cursor()

        cursor.execute((query_str), (url_str, url_name, id_find))  # !!!!OK
        print('Update ', connection.total_changes)  # rowcount())#total_changes total_changes() )

        # cursor.execute((query_str))#, (reg1,))
        # cursor.execute((query_str), (reg_in,))
        # str30 OK!!!!
        # cursor.execute((query_str_3), (reg1, reg2))
        # str31 list_str OK!!!!
        # cursor.execute((query_str_3), (list_str))
        # str32 trupl_str OK!!!!
        # cursor.execute((query_str_3), (trupl_str))
        # str4 OK dict_str!!!!
        # cursor.execute((query_str_4), (dict_str))  # [0], val[1]))
        # str5 OK sql динамически сформирован весь запрос!!!!
        # cursor.execute((sql), (params))
        # cursor.execute(sql, (params))#[0], val[1]))
        # cursor.execute("""
        # SELECT name FROM regions WHERE name LIKE ? ORDER BY name
        #   """, (reg1,))
        # result = cursor.fetchone()
        # result = cursor.fetchall()
        # print(f'result cursor.fetchall() = {len(result)} {result}')
        connection.commit()
    ##connection.close()


def parse_cat_xml(dict_cat): #(id_kod, name_rus=""):

    with open("Data/get_categories2.html", 'r', encoding='utf-8') as file:
        r = file.read()
        html_txt = r  # resp_text  # response.text
    # Blok
    # path_blok = './/div//div//div//ul[@data-marker="rubricator/list"]//ul//a[substring(@class,1,25) ="rubricator-list-item-link"]'
    # path_items = './/a[substring(@class,1,25) ="rubricator-list-item-link"]'
    # path_items_full = './/div//div//div//ul[@data-marker="rubricator/list"]//ul//a[@data-category-id>"0"]'
    # substring(@class,1,13) ="iva-item-text"
    #str_name=str("'"+name_rus+"'")

    path_name_cat = './/text()'
    path_url = './/@href'
    path_cat_id = './/@data-category-id'
    stop1 = 'evaluation'
    stop2 = 'catalog '

    tree = html.fromstring(html_txt)

    for cat_item in dict_cat:
        name_rus = cat_item['name']
        id_kod = cat_item['id']
        print(name_rus)

        str_name = str("'" + name_rus + "'")
        path_items_find_name = f".//div//div//div//ul[@data-marker='rubricator/list']//ul//a[text()={str_name}]"
        path_items_find_id = f'.//div//div//div//ul[@data-marker="rubricator/list"]//ul//a[@data-category-id={id_kod}]'

        print(f'name_rus {name_rus} ========================= path_items_find {path_items_find_id}')
        print(f'path_items_find_name == {path_items_find_name}')
        # tree.xpath(path_items_find)
        f = 1

#        if f == 1:

        # for item in tree.xpath(path_items_full): #html.fromstring(html_txt):
        try:
            item = tree.xpath(path_items_find_id)[0]
            #item = tree.xpath(path_items_find_name)[0]
            #print(item)
        except:
            continue
        #item = tree.xpath(path_items_find_name)[0]
        print(item)
        name = item.xpath(path_name_cat)
        cat_id = item.xpath(path_cat_id)
        url = item.xpath(path_url)  # [0]
        url_pars1 = urlparse(url[-1])
        path_url1 = url_pars1[2]
        dirLst = path_url1.split("/")
        dirname_city1 = dirLst[1]
        dirname_cat1 = dirLst[2]
        print(f'xpath_name {name} , cat_id {cat_id}, url {url}, dirname_cat1 {dirname_cat1}')
        if (stop1 in dirname_city1) or ((stop2 in dirname_city1)) or (len(dirLst) < 3):
            return
        check_category_path(cat_id, dirname_cat1, name)
        #
        # print(f'dirLst {len(dirLst)} = {dirLst}  url = {url}')
        # print(f'  name {name} @@@@@@@@ Cat_id = {cat_id}  dirname_cat = {dirname_cat1} \n')

        # print(f'dirname = {dirname1}')
    # ! В HTML карточке объявления путь к ID City
    # https://www.avito.ru/bryansk/zapchasti_i_aksessuary/dvigatel_na_skuter_150_kubov_157qmj_2332435829
    # //*[@id="app"]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div/div[3]
    # XPATH = .//div//div//div[@data-map-type='dynamic']

    # data-item-id="2332435829" ID объявления
    # data-location-id="623880" ID City
    # data-category-id="10" ID Kategory

    # tree = html.fromstring(html_txt)
    # index = 0

    # items_lxml = tree.xpath(path)[0]
    # for item_lxml in items_lxml:
    #     desript = item_lxml.xpath('//meta[@itemprop="description"]')
    #     # getting movie id
    #     movie_link = item_lxml.xpath('.//div[@class = "nameRus"]/a/@href')[0]


def get_file_new():
    # with open("Data/get_categories1.html", 'r', encoding='utf-8') as file:
    with open("Data/get_categories2.html", 'r', encoding='utf-8') as file:
        r = file.read()
        #   print(r)
        #parse_cat_xml(r)
        # print(r)
        return r




'''
# (UPDATE table1 SET url_name = ? WHERE id = ), (url_str, id_find) ;
# UPDATE table1 SET name = ‘Людмила Иванова’ WHERE id = 2;
#
# Убедимся, что модификация данных прошла успешно, выполнив команду SELECT:
# sqlite> SELECT * FROM table1;
# 2|Людмила Иванова|21|Бухгалтер|35232.2
'''


def search_category_id(id):
    print('Function search_category_id')
    reg_in = id
    reg1 = reg_in + "%"
    reg2 = "%" + reg_in.lower() + "%"
    trupl_str = (reg1, reg2)
    print(f'trupl_str {trupl_str}')

    list_str = []
    list_str.append(reg1)
    list_str.append(reg2)
    print(f"list_str {list_str}")

    dict_str = dict()

    values = [reg1, reg2]
    values = [reg_in, reg_in]

    param_names = [f"reg{i + 1}" for i in range(len(values))]
    in_str = ", ".join(":" + p for p in param_names)  # print(",".join("Python")) >>>P,y,t,h,o,n
    params = dict(zip(param_names, values))

    sql = f"""SELECT name, id FROM categories
                 WHERE id in ({in_str}) ORDER BY id"""
    print(f'params {params} , in_str {in_str},\n sql= {sql}')
    dict_str.setdefault("reg1", reg1)  # append("reg1",reg1) # + reg2
    dict_str.setdefault("reg2", reg2)  # append("reg1",reg1) # + reg2
    # val.append("reg2", reg2)
    # for key, value in values:
    #    countries_hdi[key] = value
    print(f'ПОИСК dict_str {dict_str["reg1"]} и {dict_str["reg2"]} ')

    with sqlite3.connect('realty.db') as connection:
        cursor = connection.cursor()
        # sql = ("CREATE INDEX index_my_table ON my_table (Field1, field2)")
        query_str = """
            SELECT name, id FROM categories WHERE id LIKE ? ORDER BY id
              """
        # Без регистра: like lower('%value%');
        # Для исключения символов: where column regexp '^[A-Za-z0-9]+$'
        # where lover(column_name) regexp '^[a-zа-яё]+$';
        # SELECT *FROM [table] WHERE ([table].[column] like <parameter>) OR (<parameter> = '%')

        query_str_3 = """
            SELECT name, id FROM categories WHERE (lower(id) LIKE ?) OR (lower(id) LIKE ?) ORDER BY id 
              """

        query_str_4 = """
            SELECT name, id FROM categories WHERE (lower(id) LIKE :reg1) OR (lower(id) LIKE :reg2) ORDER BY id 
              """

        query_str_5 = sql
        # """
        # SELECT name, id FROM categories WHERE (lower(id) LIKE ?) OR (lower(id) LIKE ?) ORDER BY id
        #   """

        # str переменные
        # cursor.execute((query_str),(reg1,))
        # cursor.execute((query_str), (reg_in,))
        # str30 OK!!!!
        # cursor.execute((query_str_3), (reg1, reg2))
        # str31 list_str OK!!!!
        # cursor.execute((query_str_3), (list_str))
        # str32 trupl_str OK!!!!
        # cursor.execute((query_str_3), (trupl_str))
        # str4 OK dict_str!!!!
        # cursor.execute((query_str_4), (dict_str))  # [0], val[1]))
        # str5 OK sql динамически сформирован весь запрос!!!!
        # cursor.execute((query_str_5), (params))
        cursor.execute((query_str_5), (params))
        # [0], val[1]))
        # cursor.execute("""
        # SELECT name FROM regions WHERE name LIKE ? ORDER BY name
        #   """, (reg1,))
        result = cursor.fetchone()
        #result = cursor.fetchall()
        print(f'result cursor.fetchone() = {len(result)} {result}')
        # print(result[0])


def search_category_name(name):
    reg_in = name
    reg1 = reg_in + "%"
    reg2 = "%" + reg_in.lower() + "%"
    trupl_str = (reg1, reg2)
    print(f'trupl_str {trupl_str}')

    list_str = []
    list_str.append(reg1)
    list_str.append(reg2)
    print(f"list_str {list_str}")

    dict_str = dict()
    values = [reg1, reg2]

    param_names = [f"reg{i + 1}" for i in range(len(values))]
    in_str = ", ".join(":" + p for p in param_names)  # print(",".join("Python")) >>>P,y,t,h,o,n
    params = dict(zip(param_names, values))

    sql = f"""SELECT name, id FROM categories
             WHERE name in ({in_str})"""
    print(f'params {params} , in_str {in_str}, sql {sql}')
    dict_str.setdefault("reg1", reg1)  # append("reg1",reg1) # + reg2
    dict_str.setdefault("reg2", reg2)  # append("reg1",reg1) # + reg2
    # val.append("reg2", reg2)
    # for key, value in values:
    #    countries_hdi[key] = value
    print(f'ПОИСК dict_str {dict_str["reg1"]} и {dict_str["reg2"]} ')

    with sqlite3.connect('realty.db') as connection:
        cursor = connection.cursor()
        # sql = ("CREATE INDEX index_my_table ON my_table (Field1, field2)")
        query_str = """
        SELECT name, id FROM categories WHERE name LIKE ? ORDER BY name
          """
        # Без регистра: like lower('%value%');
        # Для исключения символов: where column regexp '^[A-Za-z0-9]+$'
        # where lover(column_name) regexp '^[a-zа-яё]+$';
        # SELECT *FROM [table] WHERE ([table].[column] like <parameter>) OR (<parameter> = '%')

        query_str_3 = """
        SELECT name, id FROM categories WHERE (lower(name) LIKE ?) OR (lower(name) LIKE ?) ORDER BY name 
          """

        query_str_4 = """
        SELECT name, id FROM categories WHERE (lower(name) LIKE :reg1) OR (lower(name) LIKE :reg2) ORDER BY name 
          """

        query_str_5 = """
         SELECT name, id FROM categories WHERE (lower(name) LIKE ?) OR (lower(name) LIKE ?) ORDER BY name 
           """

        # str переменные
        # cursor.execute((query_str),(reg1,))
        cursor.execute((query_str), (reg_in,))
        # str30 OK!!!!
        # cursor.execute((query_str_3), (reg1, reg2))
        # str31 list_str OK!!!!
        # cursor.execute((query_str_3), (list_str))
        # str32 trupl_str OK!!!!
        # cursor.execute((query_str_3), (trupl_str))
        # str4 OK dict_str!!!!
        # cursor.execute((query_str_4), (dict_str))  # [0], val[1]))
        # str5 OK sql динамически сформирован весь запрос!!!!
        # cursor.execute(sql, (params))#[0], val[1]))
        # cursor.execute("""
        # SELECT name FROM regions WHERE name LIKE ? ORDER BY name
        #   """, (reg1,))
        result = cursor.fetchone()
        # result = cursor.fetchall()
        print(f'result cursor.fetchall() = {len(result)} {result}')
        # print(result[0])


def find_id_cat_from_dict(dict_list):

    print('find_id_cat_from_dict')
    reg_in = id
    reg1 = reg_in + "%"
    reg2 = "%" + reg_in.lower() + "%"
    trupl_str = (reg1, reg2)
    print(f'trupl_str {trupl_str}')

    list_str = []
    list_str.append(reg1)
    list_str.append(reg2)
    print(f"list_str {list_str}")

    dict_str = dict()

    values = [reg1, reg2]
    values = [reg_in, reg_in]

    param_names = [f"reg{i + 1}" for i in range(len(values))]
    in_str = ", ".join(":" + p for p in param_names)  # print(",".join("Python")) >>>P,y,t,h,o,n
    params = dict(zip(param_names, values))

    sql = f"""SELECT name, id FROM categories
                 WHERE id in ({in_str}) ORDER BY id"""
    print(f'params {params} , in_str {in_str},\n sql= {sql}')
    dict_str.setdefault("reg1", reg1)  # append("reg1",reg1) # + reg2
    dict_str.setdefault("reg2", reg2)  # append("reg1",reg1) # + reg2
    # val.append("reg2", reg2)
    # for key, value in values:
    #    countries_hdi[key] = value
    print(f'ПОИСК dict_str {dict_str["reg1"]} и {dict_str["reg2"]} ')

    with sqlite3.connect('realty.db') as connection:
        cursor = connection.cursor()
        # sql = ("CREATE INDEX index_my_table ON my_table (Field1, field2)")
        query_str = """
            SELECT name, id FROM categories WHERE id LIKE ? ORDER BY id
              """
        # Без регистра: like lower('%value%');
        # Для исключения символов: where column regexp '^[A-Za-z0-9]+$'
        # where lover(column_name) regexp '^[a-zа-яё]+$';
        # SELECT *FROM [table] WHERE ([table].[column] like <parameter>) OR (<parameter> = '%')

        query_str_3 = """
            SELECT name, id FROM categories WHERE (lower(id) LIKE ?) OR (lower(id) LIKE ?) ORDER BY id 
              """

        query_str_4 = """
            SELECT name, id FROM categories WHERE (lower(id) LIKE :reg1) OR (lower(id) LIKE :reg2) ORDER BY id 
              """

        query_str_5 = sql
        # """
        # SELECT name, id FROM categories WHERE (lower(id) LIKE ?) OR (lower(id) LIKE ?) ORDER BY id
        #   """

        # str переменные
        # cursor.execute((query_str),(reg1,))
        # cursor.execute((query_str), (reg_in,))
        # str30 OK!!!!
        # cursor.execute((query_str_3), (reg1, reg2))
        # str31 list_str OK!!!!
        # cursor.execute((query_str_3), (list_str))
        # str32 trupl_str OK!!!!
        # cursor.execute((query_str_3), (trupl_str))
        # str4 OK dict_str!!!!
        # cursor.execute((query_str_4), (dict_str))  # [0], val[1]))
        # str5 OK sql динамически сформирован весь запрос!!!!
        # cursor.execute((query_str_5), (params))
        cursor.execute((query_str_5), (params))
        # [0], val[1]))
        # cursor.execute("""
        # SELECT name FROM regions WHERE name LIKE ? ORDER BY name
        #   """, (reg1,))
        # result = cursor.fetchone()
        result = cursor.fetchall()
        print(f'result cursor.fetchall() = {len(result)} {result}')
        # print(result[0])
    #print(id_kod)


def list_id_to_db(dict_list):
    dict_list = dict_list
    pprint(dict_list)  # , depth=0)

    find_id_cat_from_dict(dict_list)
    # for i in dict_list:
    #     id_kod = i["id"]
    #
    #     find_id_cat_from_dict(id_kod, dict_list)
    #
    #     print(f' {id_kod} , {i["name"]}, {i["url_name"]}')  # получаем значения по ключу


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        # col[0] is the column name
        d[col[0]] = row[idx]
    return d
    #         variant 2
    # fields = [column[0] for column in cursor.description]
    # return {key: value for key, value in zip(fields, row)}


def get_data_to_json():
    database = 'realty.db'
    conn = sqlite3.connect(database)  # conn.row_factory = sqlite3.Row
    conn.row_factory = dict_factory
    c = conn.cursor()
    temp = c.execute("SELECT * FROM categories")
    rst = c.fetchall()  # rst is a list of dict
    return rst #jsonify(rst)

def main():

    dict_cat = get_data_to_json()
    #pprint(dict_cat)
    list_id_to_db(dict_cat)
    parse_cat_xml(dict_cat) #id_kod, name_rus="")


def bad_categories_to_dict():
    ''' Выгружаем категории в справочник
    database = 'database.db'

with closing(sqlite3.connect(database)) as connection:
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("""select * from images""")

    row = cursor.fetchone()
    print('Объект "Row": ', row)
    print('Словарь: ', dict(row))

не обязательно преобразование в словарь.
Получить значение по ключу у класса Row:

   cursor.execute("""select * from images""")

    for i in cursor.fetchall():
       print(i['name']) # получаем значения по ключу
    '''
    # pass
    database = 'realty.db'

    with closing(sqlite3.connect(database)) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("""select * from categories""")

        # row = cursor.fetchone() # row_all = cursor.fetchall() # print('Объект "Row": ', row_all) #print('Словарь: ', len(dict(row_all)))
        d = {}
        for i in cursor.fetchall():
            print(f' {i["id"]} , {i["name"]}, {i["url_name"]}')  # получаем значения по ключу
            # print(f'{i["id"]},{i["name"]},{i["url_name"]}')  # получаем значения по ключу


if __name__ == '__main__':
    id = '14'
    url_str = 'TEST499'
    name = "Товары для компьютера"
    # search_category_name(name)
    # search_category_id(id)
    # check_category_path(id, url_str)
    # bad_categories_to_dict() #не берет первый элемент
    #get_data_to_json()
    #get_file_new()
    #parse_xml_new(id, name)
    main()
