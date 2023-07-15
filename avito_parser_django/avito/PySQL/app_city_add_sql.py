import psycopg2
import json
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def city_list_from_db():
    con = psycopg2.connect(
        database="main_avito_django_bot",
        user="postgres",
        password="postgres",
        #password=input("Пароль"),
        #host="192.168.100.9",
        host="10.10.10.18",
        port="5432"
    )

    print("Database opened successfully")
    cur = con.cursor()
    cur.execute("SELECT id, name from APARSER_city")
    #cur.execute("SELECT id, name from AVITO_city")

    rows = cur.fetchall()
    for row in rows:
        print("id =", row[0], " NAME =", row[1])
        #print("NAME =", row[1])

    print("Operation done successfully")
    con.close()

def city_from_js_to_db():
    con = psycopg2.connect(
        database="main_avito_django_bot",
        user="postgres",
        password="postgres",
        #password=input("Пароль"),
        #host="192.168.100.9",
        host="10.10.10.18",
        port="5432"
    )

    print("Database opened successfully")
    cur = con.cursor()
    with open("json/avito_city.json",'r', encoding="utf-8") as file:
        data = json.load(file)
        #print(data)
    for item in data['data']:
        #print(f"Сохраненный {item['id']} = {item['name']}")
        id_reg = item['id']
        name_reg = item['name']
        reg_id = int(item['parent_Id'])

        values = ({'id': item['id'], 'name': item['name'], 'region_id': reg_id })
        print(values)
        cur.execute(
            "INSERT INTO APARSER_CITY (id, city_id, name, region_id) VALUES (%(id)s, %(id)s,%(name)s,%(region_id)s)",
            values
        )
        #cur.execute("INSERT INTO APARSER_city (id, city_id, name, index_post, url_name, url_path, region_id, parent_id) VALUES (%(id)s,%(id)s,%(name)s,'00','blank','blank',%(region_id)s, %(parent_Id)s)", values)
        con.commit()
        print("Record inserted successfully")


# def create_city_db():
#     con = psycopg2.connect(
#         database="main_avito_django_bot",
#         user="postgres",
#         password="postgres",
#         #password=input("Пароль"),
#         #host="192.168.100.9",
#         host="10.10.10.18",
#         port="5432"
#     )
#
#     print("Database opened successfully")
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE AVITO_city
#         (id INT PRIMARY KEY NOT NULL,
#          NAME TEXT NOT NULL);''')
#
#     print("Table created successfully")
#     con.commit()
#     con.close()

if __name__ == '__main__':
    pass
    #create_city_db()
    #city_from_js_to_db()
    #city_list_from_db()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
