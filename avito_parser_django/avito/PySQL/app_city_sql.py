import psycopg2
import json
# This is a sample Python script.
#https://www.youtube.com/watch?v=h5wgbJiSy7Q
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def city_list_from_db():
    con = psycopg2.connect(
        database="main_avito_django_bot",
        user="postgres",
        password="postgres",
        #password=input("Пароль"),
        #host="192.168.100.9",
        host="192.168.88.254",
        #host="10.10.10.18",
        port="5432"
    )

    print("Database opened successfully")
    cur = con.cursor()
    cur.execute("SELECT id, name from aparser_city") #, parent_Id

    rows = cur.fetchall()
    for row in rows:
        print("id =", row[0], " NAME =", row[1]) #, "parent_Id =", row[2])
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
        print("Json opened")
    for item in data['data']:
        print(f"Сохраненный {item['id']} = {item['name']} регион {item['parent_Id']}")
        #id_reg = item['id']
        #name_reg = item['name']
        values = ({'id': item['id'], 'name': item['name'], 'parent_Id': item['parent_Id']})
        # cur.execute(
        #     "INSERT INTO AVITO_city (id,NAME,parent_Id) VALUES (%(id)s,%(name)s,%(parent_Id)s)", values
        # )
        cur.execute(
            "INSERT INTO aparser_city (id,NAME,parent_Id) VALUES (%(id)s,%(name)s,%(parent_Id)s)", values
        )

#        values = ({'id': 1, 'name': 'Vasya', 'age': 45})
#        cursor.execute("INSERT INTO tableName(id, name, age) VALUES (%(id)s,%(name)s,%(age)s)", values)
        con.commit()
        print("Record inserted successfully")

#input("Пароль"),
def create_city_db_sql():
    pass
    # con = psycopg2.connect(
    #     database="main_avito_django_bot",
    #     user="postgres",
    #     password="postgres",
    #     #password=input("Пароль"),
    #     #host="192.168.100.9",
    #     host="10.10.10.18",
    #     port="5432"
    # )
    #
    # print("Database opened successfully")
    #
    # cur = con.cursor()
    # cur.execute('''
    #     CREATE TABLE AVITO_city
    #     (id INT PRIMARY KEY NOT NULL,
    #      name TEXT NOT NULL,
    #      parent_Id INT NOT NULL,
    #      url_path TEXT ,
    #      url_name TEXT ,
    #      index_post INT
    #      )
    #      ''')
    #
    # print("Table created successfully")
    # con.commit()
    # con.close()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #create_city_db_sql()
    print('start')
    #city_from_js_to_db()
    city_list_from_db()

    #city_list_from_db()



##!/usr / bin / python
#
# import psycopg2
# from config import config
#
#
# def create_tables():
#     """ create tables in the PostgreSQL database"""
#     commands = (
#         """
#         CREATE TABLE vendors (
#             vendor_id SERIAL PRIMARY KEY,
#             vendor_name VARCHAR(255) NOT NULL
#         )
#         """,
#         """ CREATE TABLE parts (
#                 part_id SERIAL PRIMARY KEY,
#                 part_name VARCHAR(255) NOT NULL
#                 )
#         """,
#         """
#         CREATE TABLE part_drawings (
#                 part_id INTEGER PRIMARY KEY,
#                 file_extension VARCHAR(5) NOT NULL,
#                 drawing_data BYTEA NOT NULL,
#                 FOREIGN KEY (part_id)
#                 REFERENCES parts (part_id)
#                 ON UPDATE CASCADE ON DELETE CASCADE
#         )
#         """,
#         """
#         CREATE TABLE vendor_parts (
#                 vendor_id INTEGER NOT NULL,
#                 part_id INTEGER NOT NULL,
#                 PRIMARY KEY (vendor_id, part_id),
#                 FOREIGN KEY (vendor_id)
#                     REFERENCES vendors (vendor_id)
#                     ON UPDATE CASCADE ON DELETE CASCADE,
#                 FOREIGN KEY (part_id)
#                     REFERENCES parts (part_id)
#                     ON UPDATE CASCADE ON DELETE CASCADE
#         )
#         """)
#     conn = None
#     try:
#         # read the connection parameters
#         params = config()
#         # connect to the PostgreSQL server
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()
#         # create table one by one
#         for command in commands:
#             cur.execute(command)
#         # close communication with the PostgreSQL database server
#         cur.close()
#         # commit the changes
#         conn.commit()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#
#
# if __name__ == '__main__':
#     create_tables()