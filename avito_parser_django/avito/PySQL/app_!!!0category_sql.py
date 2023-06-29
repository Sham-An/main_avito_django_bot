import psycopg2
import json


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def category_add(id, name, parentId):
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

    #models = Category
    #cat = Category.get(pk=id)
    print("ADD CATEGORY ", id, name, parentId)
    values = ({'id': id, 'name': name, 'region_id': parentId})

    cur.execute(
        "INSERT INTO APARSER_CATEGORY (id, cat_kod, name, parent_kod, url_path,url_name) VALUES (%(id)s, %(id)s,%(name)s,%(region_id)s,'blank','blank')",
        values
    )
    # cur.execute("INSERT INTO APARSER_city (id, city_id, name, index_post, url_name, url_path, region_id, parent_id) VALUES (%(id)s,%(id)s,%(name)s,'00','blank','blank',%(region_id)s, %(parent_Id)s)", values)
    con.commit()


# #
# #  #   PAGE_LIMIT = 10
# #      try:
# #         p = Category.objects.get(url=url)
# #         p.task = self.task
# #         p.title = title
# #         p.price = price
# #         p.currency = currency
# #         p.save()
# #     except Product.DoesNotExist:
#         p = Category(
#             pk = pk,
#             name = name,
#             parent_Id = parent_Id,
#             JsId = JsId,
#             # task=self.task,
#             # url=url,
#             # title=title,
#             # price=price,
#             # currency=currency,
#             # published_date=date,
#         ).create()
#
#     logger.debug(f'product {p}')



def list_category(data):
    all_id = []
    print("___________22 LIST_DICT 22________________")
    for dataitems in data['categories']:
        print(dataitems['id'], dataitems['name'])
        print(dataitems)
        all_id.append(dataitems['id'])
        # print(type(dataitems['id']))
        id = dataitems['id']
        name = dataitems['name']
        parentId = 0
        print("PARENT!!!! =", id, name, parentId)
        category_add(id, name, parentId)
#        category_add(id, name, parentId)
        if dataitems['id'] > 0:
            for datainfo in dataitems['children']:
                if datainfo['id'] in all_id:
                    print('IIIIDDDD Поймали ДУБЛЯЖ')
                    break
                all_id.append(datainfo['id'])
                # if 'Ипот' in datainfo['name']:
                #    print('Поймали ИПОТЕКУ')
                # break
                id = datainfo['id']
                name = datainfo['name']
                parentId = datainfo['parentId']
                print(id, name, parentId)
                # print(datainfo['id'], datainfo['name'], datainfo['parentId'])
                category_add(id, name, parentId)
    all_id.sort()
    print(all_id)
    # except AttributeError:


def Open_json_category():

    with open("json/avito_category.json", encoding='utf-8') as file:
        data = json.load(file)
        # list_dict(data)
        list_category(data)
        #print(data)


def category_list_from_db():
    con = psycopg2.connect(
        database="main_avito_django_bot",
        user="postgres",
        password="postgres",
        # password=input("Пароль"),
        # host="192.168.100.9",
        host="10.10.10.18",
        port="5432"
    )

    print("Database opened successfully")
    cur = con.cursor()
    cur.execute("SELECT id, name from APARSER_city")
    # cur.execute("SELECT id, name from AVITO_city")

    rows = cur.fetchall()
    for row in rows:
        print("id =", row[0], " NAME =", row[1])
        # print("NAME =", row[1])

    print("Operation done successfully")
    con.close()


def category_from_js_to_db():
    con = psycopg2.connect(
        database="main_avito_django_bot",
        user="postgres",
        password="postgres",
        # password=input("Пароль"),
        # host="192.168.100.9",
        host="10.10.10.18",
        port="5432"
    )

    print("Database opened successfully")
    cur = con.cursor()
    with open("json/avito_category.json", 'r', encoding="utf-8") as file:
        data = json.load(file)
        print(data)
    # for item in data['data']:
    #     #print(f"Сохраненный {item['id']} = {item['name']}")
    #     #id_reg = item['id']
    #     #name_reg = item['name']
    #     reg_id = int(item['parent_Id'])
    #
    #     values = ({'id': item['id'], 'name': item['name'], 'region_id': reg_id })
    #     print(values)
    #     cur.execute(
    #         "INSERT INTO APARSER_CITY (id, city_id, name, region_id) VALUES (%(id)s, %(id)s,%(name)s,%(region_id)s)",
    #         values
    #     )
    #     #cur.execute("INSERT INTO APARSER_city (id, city_id, name, index_post, url_name, url_path, region_id, parent_id) VALUES (%(id)s,%(id)s,%(name)s,'00','blank','blank',%(region_id)s, %(parent_Id)s)", values)
    #     con.commit()
    #     print("Record inserted successfully")


if __name__ == '__main__':
    # create_city_db()
    Open_json_category()
    #category_from_js_to_db()
    # city_list_from_db()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
