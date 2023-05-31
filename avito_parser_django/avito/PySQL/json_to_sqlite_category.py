import copy
import json
import sqlite3
from datetime import datetime
import pandas as pd
import json
import pprint

"""
Чтобы проверить, есть ли указанный ключ в словаре, используйте ключевое слово in или метод get словаря:
the_dict = {"a": 1, "b": 2}
print("c" in the_dict)
>False
print("a" in the_dict)
>True

dictionary = {'A': 1, 'B': 2, 'C': 3}
key = 'B'
if key in dictionary:
    print("Key", key, "exists in the dictionary")
else:
    print("Key doesn't exist in the dictionary")
 

The in оператор реализует встроенную функцию __contains__. Однако вызывать __contains__ напрямую. in оператор — это Pythonic способ вызвать __contains__ функция.
    dictionary = {'A': 1, 'B': 2, 'C': 3}
    key = 'B'
    value = dictionary.__contains__(key)
    if value:
        print("Key", key, "exists in the dictionary")
    else:
        print("Key doesn't exist in the dictionary")
 


Метод get объекта словаря возвращает найденное значение в словаре по ключу. Или значение, указанное как стандартное возвращаемое, — если ключ не найден:
the_dict = {"a": 1, "b": 2}
if not the_dict.get("A", None):
    print("Такой ключ не найден")
>Такой ключ не найден

a = the_dict.get("a", None)
print(a)
>1

4. Использование setdefault() функция
Наконец, вы можете использовать встроенную функцию setdefault(), 
который вставляет ключ, только если он не найден в словаре. 
Это особенно полезно, когда вам нужно вставить ключ, 
только если он еще не существует в словаре.

if __name__ == '__main__':
 
    dictionary = {'A': 1, 'B': 2, 'C': 3}
    key = 'B'
 
    value = dictionary.setdefault(key)
 
    if value:
        print("Key", key, "exists in the dictionary")
    else:
        print("Key doesn't exist in the dictionary")
 
###########################################################
Метод dict.setdefault() вернет значение словаря dict, соответствующее ключу key.
Если указанный ключ key отсутствует, вставит его в словарь dict со значением default и вернет значение default.
Если значение по умолчанию default не установлено и ключ отсутствует, метод вставит ключ в словарь со значением None, при этом никакое значение не возвращается.
По умолчанию default имеет значение None. 

Этот метод никогда не вызывает исключения KeyError.


Пример работы МЕТОДА словаря dict.setdefault():
>>> x = {'one': 0, 'two': 20, 'three': 3, 'four': 4}
>>> x.setdefault('one')
# 0

>>> x.setdefault('ten')
>>> x
# {'one': 0, 'two': 20, 'three': 3, 'four': 4, 'ten': None}

>>> x.setdefault('six', 6)
# 6
>>> x
# {'one': 0, 'two': 20, 'three': 3, 'four': 4, 'ten': None, 'six': 6}

>>> x.setdefault('six', 10)
# 6
>>> x
# {'one': 0, 'two': 20, 'three': 3, 'four': 4, 'ten': None, 'six': 6} 

"""


# import sqlite


def open_file_category():
    # Открываем файл
    with open("avito_category.json", encoding='utf-8') as file:  # Без указания кодировки выдает ошибку
        data = json.load(file)  # loadS из строки, load из файла

    data_1 = data['categories']
    child_1 = []
    #
    parent_list = []
    child_list = []
    # print(data_1)
    for item in data_1:  # ['data']:
        item.setdefault('children', child_1)
        item.setdefault('parentId')  # , "non")

        parent_clean = copy.deepcopy(item)
        parent_clean.pop('showMap', "")
        child = parent_clean.pop('children', child_1)
        parent_clean.setdefault('children', len(child))

        print(f'parent_clean = {parent_clean} child_clean = {child}')
        parent_list.append(parent_clean)
        if child:  # != 'non':
            for i in child:  # item['children']:
                i.setdefault('children', "-")
                i.setdefault('parentId')  # , "non")
                i.pop('showMap')
                # print(type(item['children']))
                print('      !!!!      ', i)
                child_list.append(i)

    df1 = pd.DataFrame(parent_list)
    df2 = pd.DataFrame(child_list)
    pprint.pprint(df1)  # , '\n\n')

    print('\n\n', df2)
    conn = sqlite3.connect("region.db")
    c = conn.cursor()
    df1.to_sql("parent_cat", conn, if_exists="replace", index=False, index_label='id')
    createSecondaryIndex = "CREATE INDEX key_3 ON parent_cat(id)"
    conn.execute(createSecondaryIndex)
    df2.to_sql("category", conn, if_exists="replace", index=False, index_label='parentId')
    createSecondaryIndex = "CREATE INDEX key_4 ON category(parentId)"
    conn.execute(createSecondaryIndex)


def open_json_data():
    conn = sqlite3.connect("region.db")

    # data.to_sql('table_name', con=engine, schema = 'dbo', if_exists='replace')

    data = list(open_file_category())
    print(type(data))
    # Create A DataFrame From the JSON Data
    df = pd.DataFrame(data)  # , index='id')
    # conn = sqlite3.connect("data.db")
    # conn = sqlite3.connect("region.db")
    c = conn.cursor()
    # df = pd.DataFrame(tuples_list, columns = ['Courses', 'Fee', 'Duration'])
    df.to_sql("region", conn, index=False, index_label='id')  # , index_label='id')#,  index_col='id'
    createSecondaryIndex = "CREATE INDEX key_1 ON region(id)"
    conn.execute(createSecondaryIndex)
    # CREATE INDEX IF NOT EXISTS dbname.ixname ON tblname (columnname) WHERE…
    # CREATE INDEX i_name ON table1 (column_name) WHERE column_name IS NOT NULL;
    # CREATE INDEX id_key ON table1 (column_name) WHERE column_name IS NOT NULL;
    # createSecondaryIndex = "CREATE INDEX index_part_name ON parts(name)"
    # sqliteCursor.execute(createSecondaryIndex)


open_file_category()
# open_json_data()

# index=False, index_label=‘id’
# Если имя первичного ключа в вашей базе данныхindexВам не нужно устанавливать эти два элемента, если нет, установите в соответствии с именем первичного ключа!

# DataFrame.to_sql(
#     name,
#     con,
#     schema=None,
#     if_exists=‘replace’ #‘fail’, ‘replace’, ‘append’
#     index=True,
#     index_label=None,
#     chunksize=None,
#     dtype=None,
#     method=None
# )


# 1. Quick Examples of pandas Set Index Name
# In case you hurry, below are some quick examples of how to set the index name to pandas DataFrame.
#
#
# # Below are quick example
# # Get name of the index column of DataFrame.
# index_name=df.index.name
#
# # set Index Name
# df.index.name='Index1'
#
# # Set column as Index.
# df = pd.DataFrame(technologies).set_index('Courses')
#
# # Rename Index.
# df = df.rename_axis('Courses1')
#
# # Get pandas index title/name by index and columns parameter.
# df = df.rename_axis(index='Courses', columns="Courses1")
#
# # Removing index and columns names to set it none.
# df = df.rename_axis(index=None, columns=None)
#
# # Using df.index.rename get pandas index title/name.
# df.index.rename('Courses1', inplace=True)
#
# # Add Multilevel index using set_index()
# df2 = df.set_index(['Courses', 'Duration'], append=True)
#
# # Rename Single index from multi Level
# df2.index = df2.index.set_names('Courses_Duration', level=2)
#
# # Rename All indexes
# df2.index=df2.index.rename(['Index','Courses_Name','Courses_Duration'])
