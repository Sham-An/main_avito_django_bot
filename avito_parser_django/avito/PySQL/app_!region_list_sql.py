import psycopg2
import json
from config import params
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def region_list_from_db():
    # con = psycopg2.connect(
    #     database="main_avito_django_bot",
    #     user="postgres",
    #     password="postgres",
    #     #password=input("Пароль"),
    #     #host="192.168.100.9",
    #     host="10.10.10.18",
    #     port="5432"
    # )
    con = psycopg2.connect(**params)

    print("Database opened successfully")
    cur = con.cursor()
    cur.execute("SELECT id, name from APARSER_REGION")
    #cur.execute("SELECT id, name from AVITO_REGION")

    rows = cur.fetchall()
    for row in rows:
        print("id =", row[0], " NAME =", row[1])
        #print("NAME =", row[1])

    print("Operation done successfully")
    con.close()

def region_from_js_to_db():
    con = psycopg2.connect(**params)

    print("Database opened successfully")
    cur = con.cursor()
    with open("json/avito_region.json",'r', encoding="utf-8") as file:
        data = json.load(file)
    for item in data['data']:
        print(f"Сохраненный {item['id']} = {item['name']}")
        id_reg = item['id']
        name_reg = item['name']
        values = ({'id': item['id'], 'name': item['name']})
        cur.execute(
            "INSERT INTO APARSER_REGION (id,region_id,kod_region,url_path,url_name,index_post,NAME) VALUES (%(id)s,%(id)s,'00','blank','blank','000000',%(name)s)", values
        )

        #con.commit()
        print("Record inserted successfully")


def create_region_db():
    con = psycopg2.connect(**params)

    print("Database opened successfully")
    cur = con.cursor()
    cur.execute('''CREATE TABLE AVITO_REGION
        (id INT PRIMARY KEY NOT NULL,
         NAME TEXT NOT NULL);''')

    print("Table created successfully")
    #con.commit()
    con.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #create_region_db()
    #region_from_js_to_db()
    region_list_from_db()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
