import json
import sqlite3
import time
import requests
from config import token, chat_id


def realty_ok():
    str = "realty_ok"

    return str


def create_category_tab():
    '''Создаем базу категории и в неё загружаем словарь'''
    # "id": 9,
    # "name": "Товары",
    # "parentId": 1,
    # "showMap": false
    # connection = sqlite3.connect('db.sqlite')
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


def check_categories(cat):
    print(cat)
    # cat1 = cat
    # cat = {'id': 116, 'name': 'Готовый бизнес', 'parentId': 8, 'showMap': False}
    cat_id = cat["id"]
    print(cat_id)
    print('check_category\n')
    # print(cat)
    with sqlite3.connect('realty.db') as connection:
        cursor = connection.cursor()
        # cur3.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user) conn.commit()
        cursor.execute("""
              SELECT id FROM categories WHERE id = (?)
          """, (cat_id,))
        result = cursor.fetchone()
        print(f'result cursor.fetchone() = {result}')

        if result is None:
            with sqlite3.connect('realty.db') as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO categories 
                    VALUES (:id, :name, :parentId, :showMap, :url_path, :url_name
                    )
                    """, cat)
                connection.commit()

        print(f'Объявление {cat_id} добавлено в базу данных')
    connection.close()

def get_cat_from_file():
    with open("avito_category.json", encoding='utf-8') as file:
        data = json.load(file)
        # list_dict(data)
        # list_category(data)
        # print(f'children === {children}')

    name = "no name"
    all_id = []
    add_cat = {'url_name': '', }
    add_cat2 = {'url_path': '', }
    for dataitems in data['categories']:
        # print(dataitems['id'], dataitems['name'])

        dataitems_copy = dataitems.copy()
        if 'children' in dataitems_copy:
            #dataitems_copy.setdefault('name_dir_en')  # , value)
            dataitems_copy.setdefault('url_path', "")
            dataitems_copy.setdefault('url_name', "")  # , value)
            dataitems_copy.setdefault('parentId', 0)  # , value)
            dataitems_copy.pop('children')
            print(f'dataitems PARENT {dataitems_copy}')
            check_categories(dataitems_copy)

        all_id.append(dataitems['id'])
        if dataitems['id'] > 0:
            for datainfo in dataitems['children']:
                if datainfo['id'] in all_id:
                    print(f'IIIIDDDD Поймали ДУБЛЯЖ {datainfo}')
                    name = datainfo['name']
                    # break
                    continue
                all_id.append(datainfo['id'])
                datainfo.update(add_cat)
                datainfo.update(add_cat2)
                print(f'CHILDREN {datainfo}')
                check_categories(datainfo)
    all_id.sort()
    print(all_id)
    # print(datainfo['id'], datainfo['name'], datainfo['parentId'])
    print(datainfo)
    return 1  # cat


def check_database(offer):
    print('check_database\n')
    print(offer)

    offer_id = offer["offer_id"]
    print(type(offer))
    with sqlite3.connect('realty.db') as connection:
        cursor = connection.cursor()
        # cur3.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
        # conn.commit()
        cursor.execute("""
            SELECT offer_id FROM offers WHERE offer_id = (?)
        """, (offer_id))
        result = cursor.fetchone()
        print(f'result cursor.fetchone() = {result}')

        if result is None:
            # send_telegram(offer)
            # ok cursor.execute("INSERT INTO offers VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", user)
            # """ #: id_item,: category_name,: category_kod) """, offer)
            # ok connection.commit()
            # c.execute("INSERT INTO stocks VALUES (?,?,?)", [dict["id"], dict["name"], dict["dob"]])

            cursor.execute("""
                INSERT INTO offers 
                VALUES (NULL, :id_item, :category_name, :category_kod, 
                :date, :time, :title_desk, :title_full, :img, :price,
                :address, :coords, :url, :uri, :uri_mweb, :offer_id, :area,
                :rooms, :floor, :total_floor)
                """, offer)
            connection.commit()
            print(f'Объявление {offer_id} добавлено в базу данных')

def check_database_old(offer):
    print('check_database')
    offer_id = offer["offer_id"]
    # print(offer_id)
    with sqlite3.connect('realty.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT offer_id FROM offers WHERE offer_id = (?)
        """, (offer_id,))
        result = cursor.fetchone()
        print(f'result cursor.fetchone() = {result}')
        if result is None:
            # send_telegram(offer)
            cursor.execute("""
                INSERT INTO offers
                VALUES (NULL,: id_item,: category_name,: category_kod,
                : date,: time,: title_desk,: title_full,: img,: price,
                : address,: coords,: url,: uri_mweb,: offer_id,: area,
                : rooms,: floor,: total_floor)
            """, offer)

            # VALUES(NULL,: url,:offer_id,: date,:price,
            # : address,:area,: rooms,:floor,: total_floor)

            # (NULL,: url,:offer_id,: date,:price,: address,: area,: rooms,:floor,: total_floor)
            #  id, id_item,: category_name,: category_kod,: date,: time,: title_desk,: title_full,: img,: price,: address,: coords,: url,: uri_mweb,: offer_id,: area,: rooms floor,: total_floor
            connection.commit()
            print(f'Объявление {offer_id} добавлено в базу данных')


def format_text(offer):
    title = f"{offer['rooms']}, {offer['area']} м2, {offer['floor']}/{offer['total_floor']} эт."

    d = offer['date']
    date = f"{d[8:10]}.{d[5:7]} в {d[11:16]}"

    text = f"""{offer['price']} ₽
<a href='{offer['url']}'>{title}</a>
{offer['address']}
{date}"""

    return text


def send_telegram(offer):
    text = format_text(offer)
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'HTML'
    }
    response = requests.post(url=url, data=data)
    print(response)


def main():
    pass


if __name__ == '__main__':
    add_cat = {'name_dir_en': 'Null', 'name_url_en': 'Null', }
    cat = {'id': 91, 'name': 'Птицы', 'parentId': 35, 'showMap': False}
    cat.update(add_cat)
    # print(cat)
    # check_categories(cat)
    #create_category_tab()
    get_cat_from_file()
    #main()
