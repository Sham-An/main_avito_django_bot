import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from urllib.parse import urlparse, parse_qs
from view_task_form_QT5_GPT import Ui_MainWindow  # изменено
import psycopg2
from config_PySide import params
from urllib.parse import urlparse, parse_qs


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Get_Task.clicked.connect(self.get_task)
##############################################################
        # # Привязка обработчика событий на смену строки в таблице
        # selection_model = self.tableView.selectionModel()
        # selection_model.currentChanged.connect(self.on_selection_change)
###############################################################

        # Привязка обработчика событий на смену строки в таблице
#        selection_model = self.View_Task.selectionModel()
#        selection_model.currentChanged.connect(self.on_selection_change)


        # Настраиваем соединение с базой данных
        self.conn = psycopg2.connect(**params)
        self.cursor = self.conn.cursor()

        # Настраиваем модель таблицы
        self.model = QStandardItemModel(self.View_Task) #tableView)
        self.View_Task.setModel(self.model)
        #self.tableView.setModel(self.model)

        # Привязка обработчика событий на смену строки в таблице

        selection_model = self.View_Task.selectionModel()
        selection_model.currentChanged.connect(self.on_selection_change)

    def get_task(self):
        # Выполняем запрос к базе данных
        query_all_task = "SELECT * FROM aparser_task"
        self.cursor.execute(query_all_task)

        # Получаем данные и имена столбцов и заполняем модель таблицы
        rows = self.cursor.fetchall()
        column_names = [desc[0] for desc in self.cursor.description]
        self.model.clear()
        self.model.setColumnCount(len(column_names))
        self.model.setHorizontalHeaderLabels(column_names)
        for row in rows:
            data = [str(col) for col in row]
            self.model.appendRow([QStandardItem(d) for d in data])

    def on_selection_change(self, current, previous):
        # Получаем URL из текущей строки таблицы
        url_col = self.model.columnCount() - 1
        url = self.model.item(current.row(), url_col).text()

        # Парсим URL и выводим его компоненты
        parsed_url = urlparse(url)
        self.Path_scheme.setText(parsed_url.scheme)
        self.Path_host.setText(parsed_url.netloc)
        self.Path_parts.setText(parsed_url.path)
        self.list_Query.clear()
        query_dict = parse_qs(parsed_url.query)
        for param in query_dict:
            self.list_Query.addItem("{}: {}".format(param, query_dict[param][0]))
        self.Task_view_text.setText(parsed_url.fragment)

    def closeEvent(self, event):
        # Закрываем соединение с базой данных
        self.cursor.close()
        self.conn.close()
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())