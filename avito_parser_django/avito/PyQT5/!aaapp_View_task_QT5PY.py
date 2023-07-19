import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from view_task_form_QT5 import Ui_MainWindow
import psycopg2
from config_PySide import params
from urllib.parse import urlparse, parse_qs


def get_task_db():
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()

    # Выполнение запроса
    query_all_task = "SELECT * FROM aparser_task"
    cursor.execute(query_all_task)

    # Получение списка результатов и имен столбцов
    rows = cursor.fetchall()
    print(rows)
    column_names = [desc[0] for desc in cursor.description]

    # Закрытие соединения
    cursor.close()
    conn.close()
    return rows


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button1.clicked.connect(self.button1_clicked)
        self.fill_table()
        self.Get_Task.clicked.connect(self.get_task)

    def fill_table(self):
        model = QStandardItemModel(self.View_Task)
        self.View_Task.setModel(model)

        data = [
            ['Получите задания', 0, 0],
        ]

        model.setRowCount(len(data))
        model.setColumnCount(len(data[0]))

        for i, row in enumerate(data):
            for j, value in enumerate(row):
                item = QStandardItem(str(value))
                model.setItem(i, j, item)

    def get_task(self):
        model = QStandardItemModel(self.View_Task)
        self.View_Task.setModel(model)
        data = get_task_db()

        model.setRowCount(len(data))
        model.setColumnCount(len(data[0]))

        for i, row in enumerate(data):
            for j, value in enumerate(row):
                item = QStandardItem(str(value))
                model.setItem(i, j, item)

        # Ваш код для получения данных и заполнения таблицы
        #pass

    def button1_clicked(self):
        url = self.urlLineEdit.text()  # Получаем текст из поля urlLineEdit
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
        self.slug_Scheme.setText(scheme)
        self.slug_Scheme.adjustSize()

        self.Path_parts.setText("\n".join(path_parts))
        self.Path_parts.adjustSize()

        self.Parsed_Query.setText(str(parsed_query))
        self.Parsed_Query.adjustSize()

        # Вывод результатов в QListWidget
        self.list_Query.clear()
        for key, value in parsed_query.items():
            self.list_Query.addItem(f"{key}: {value}")



        # Выводим результаты в table_Query
        self.table_Query.clear()  # Очищаем таблицу

        # Создаем нужное количество строк и столбцов
        row_count = len(parsed_query)
        column_count = 2
        self.table_Query.setRowCount(row_count)
        self.table_Query.setColumnCount(column_count)

        # row = 0
        # for key, value in parsed_query.items():
        #     # Записываем значения в ячейки таблицы
        #     key_item = QTableWidgetItem(str(key))
        #     value_item = QTableWidgetItem(str(value[0]))
        #
        #     self.table_Query.setItem(row, 0, key_item)
        #     self.table_Query.setItem(row, 1, value_item)
        #     row += 1



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# import psycopg2
# from config_PySide import params
# from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
# from PySide6.QtGui import QStandardItemModel, QStandardItem
# from view_task_form_PS6 import Ui_MainWindow
#
# def get_task():
#     conn = psycopg2.connect(**params)
#     cursor = conn.cursor()
#
#     # Выполнение запроса
#     query_all_task = "SELECT * FROM aparser_task"
#     cursor.execute(query_all_task)
#
#     # Получение списка результатов и имен столбцов
#     rows = cursor.fetchall()
#     column_names = [desc[0] for desc in cursor.description]
#
#     # Закрытие соединения
#     cursor.close()
#     conn.close()
#
#     # Получение модели таблицы View_Task
#     model = ui.View_Task.model()
#     if model is None:
#         model = QStandardItemModel()
#         ui.View_Task.setModel(model)
#
#     # Очистка и установка размера таблицы
#     model.clear()
#     model.setRowCount(len(rows))
#     model.setColumnCount(len(column_names))
#
#     # Заполнение таблицы данными
#     for i, row in enumerate(rows):
#         for j, value in enumerate(row):
#             if value is not None:
#                 item = QStandardItem(str(value))
#                 model.setItem(i, j, item)
#
# if __name__ == '__main__':
#     app = QApplication([])
#     mainwindow = QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(mainwindow)
#     mainwindow.show()
#
#     ui.Get_Task.clicked.connect(get_task)
#
#     app.exec()
