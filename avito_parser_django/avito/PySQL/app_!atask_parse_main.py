import psycopg2
from config import params

# Параметры подключения к базе данных
# params = {
#     'host': 'localhost',
#     'port': 5432,
#     'dbname': 'main_avito_django_bot',
#     'user': 'postgres',
#     'password': 'postgres'
# }
# Подключение к базе данных
conn = psycopg2.connect(**params)
cursor = conn.cursor()

# Выполнение запроса
cursor.execute("SELECT * FROM aparser_task")

# Получение списка результатов
rows = cursor.fetchall()
print(rows)
# Закрытие соединения
cursor.close()
conn.close()

# Вывод списка результатов
for row in rows:
    print("id =", row[0], " NAME =", row[1], "parent_Id =", row[2])
    # print("NAME =", row[1])

