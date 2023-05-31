import sqlite3
import time
import requests
from config import token, chat_id


def check_database(offer):
    print('check_database')
    offer_id = offer["offer_id"]
    #print(offer_id)
    with sqlite3.connect('realty_tmp.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT offer_id FROM offers WHERE offer_id = (?)
        """, (offer_id,))
        result = cursor.fetchone()
        print(f'result cursor.fetchone() = {result}')
        if result is None:
            #send_telegram(offer)
            cursor.execute("""
                INSERT INTO offers
                VALUES (NULL,: id_item,: category_name,: category_kod,
                : date,: time,: title_desk,: title_full,: img,: price,
                : address,: coords,: url,: uri_mweb,: offer_id,: area,
                : rooms,: floor,: total_floor)
            """, offer)

            # VALUES(NULL,: url,:offer_id,: date,:price,
            # : address,:area,: rooms,:floor,: total_floor)

            #(NULL,: url,:offer_id,: date,:price,: address,: area,: rooms,:floor,: total_floor)
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
    main()
