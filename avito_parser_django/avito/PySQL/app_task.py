from app_Get_cursor import PostgreSQLConnection

# Создание экземпляра класса
connection = PostgreSQLConnection(
    host='localhost',
    port=5432,
    dbname='main_avito_django_bot',
    user='postgres',
    password='postgres'
)

# Установка соединения и выполнение запроса
connection.connect()
#rows =
connection.execute_query("SELECT * FROM aparser_task")

# Получение списка результатов
rows = connection.cursor.fetchall()

# Вывод списка результатов
for row in rows:
    print("id =", row[0], " NAME =", row[1], "parent_Id =", row[2])

# Закрытие соединения
connection.close()


# cur.execute("SELECT id, name,parent_Id from AVITO_city")
#
# rows = cur.fetchall()
# for row in rows:
#     print("id =", row[0], " NAME =", row[1], "parent_Id =", row[2])
#     # print("NAME =", row[1])
#
# print("Operation done successfully")
# con.close()
