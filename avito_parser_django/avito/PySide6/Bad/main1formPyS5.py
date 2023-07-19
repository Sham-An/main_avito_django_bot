from urllib.parse import urlparse, parse_qs
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
import psycopg2
from config_PySide import params

def get_task():
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()

    # Выполнение запроса
    query_all_task = "SELECT * FROM aparser_task"
    cursor.execute(query_all_task)

    # Получение списка результатов и имен столбцов
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]

    # Закрытие соединения
    cursor.close()
    conn.close()

    # Очистка таблиц
    ui.table_Task.clearContents()
    #ui.View_Task.clearContents()

    # Заполнение таблицы table_Task
    row_count = len(rows)
    column_count = len(column_names)

    # Создание модели данных
    model = QStandardItemModel(row_count, column_count)

    for i, row in enumerate(rows):
        items = [QStandardItem(str(value)) for value in row]
        model.appendRow(items)

    # Установка модели данных в table_Task
    ui.table_Task.setModel(model)

    # Установка модели данных в View_Task
    ui.View_Task.setModel(model)

def button1_clicked():
    url = ui.urlLineEdit.text()  # Получаем текст из поля urlLineEdit
    parsed_url = urlparse(url)

    # Извлекаем составляющие адреса
    scheme = parsed_url.scheme
    netloc = parsed_url.netloc
    path = parsed_url.path
    path_parts = parsed_url.path.split("/")
    params = parsed_url.params
    query = parsed_url.query
    fragment = parsed_url.fragment

    # Парсим параметры запроса
    parsed_query = parse_qs(query)

    # Выводим результаты
    ui.slug_Scheme.setText(scheme)
    ui.slug_Scheme.adjustSize()

    ui.Path_parts.setText("\n".join(path_parts))
    ui.Path_parts.adjustSize()

    ui.Parsed_Query.setText(str(parsed_query))
    ui.Parsed_Query.adjustSize()

    # Вывод результатов в QListWidget
    ui.list_Query.clear()
    for key, value in parsed_query.items():
        ui.list_Query.addItem(f"{key}: {value}")

    # Выводим результаты в table_Query
    ui.table_Query.clear()  # Очищаем таблицу

    # Создаем нужное количество строк и столбцов
    row_count = len(parsed_query)
    column_count = 2
    ui.table_Query.setRowCount(row_count)
    ui.table_Query.setColumnCount(column_count)

    row = 0
    for key, value in parsed_query.items():
        # Записываем значения в ячейки таблицы
        key_item = QTableWidgetItem(str(key))
        value_item = QTableWidgetItem(str(value[0]))

        ui.table_Query.setItem(row, 0, key_item)
        ui.table_Query.setItem(row, 1, value_item)
        row += 1

    get_task()

app = QApplication([])
ui_file = "mainwindow.ui"
ui = QUiLoader().load(QFile(ui_file))
window = QMainWindow()
window.setWindowTitle("Task edit")
window.setCentralWidget(ui)

# Подключение функции button1_clicked к сигналу clicked кнопки button1
ui.button1.clicked.connect(button1_clicked)
ui.Get_Task.clicked.connect(get_task)

window.show()
app.exec_()

