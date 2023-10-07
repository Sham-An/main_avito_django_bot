import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QUrl
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

#        self.Copy.clicked.connect(self.button1_clicked)
        self.fill_table()
        self.Get_Task.clicked.connect(self.get_task)

        # Привязка обработчика событий на смену строки в таблице
        selection_model = self.View_Task.selectionModel()
        selection_model.currentChanged.connect(self.on_selection_change)

    def fill_table(self):
        self.model = QStandardItemModel(self.View_Task)
        self.View_Task.setModel(self.model)

        data = [
            ['Получите задания', 0, 0],
        ]

        self.model.setRowCount(len(data))
        self.model.setColumnCount(len(data[0]))

        for i, row in enumerate(data):
            for j, value in enumerate(row):
                item = QStandardItem(str(value))
                self.model.setItem(i, j, item)

    def get_task(self):
        data = get_task_db()

        self.model.setRowCount(len(data))
        self.model.setColumnCount(len(data[0]))

        for i, row in enumerate(data):
            for j, value in enumerate(row):
                item = QStandardItem(str(value))
                self.model.setItem(i, j, item)

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

    def on_selection_change(self, current, previous):
        # Получение текущей строки и третьей колонки
        column = 2  # Вторая колонка (с индексом 1)
        value = current.sibling(current.row(), column).data()

        # Парсинг URL и установка этого значения в lineEdit
        url = QUrl(value)
        self.lineEdit.setText(url.toString())

        # Возврат курсора в начало строки
        self.lineEdit.setCursorPosition(0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
