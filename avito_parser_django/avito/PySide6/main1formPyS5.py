from urllib.parse import urlparse, parse_qs
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi


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


app = QApplication([])
ui = loadUi("mainwindow.ui")
window = QMainWindow()
window.setWindowTitle("Task edit")
window.setCentralWidget(ui)

# Подключение функции button1_clicked к сигналу clicked кнопки button1
ui.button1.clicked.connect(button1_clicked)

window.show()
app.exec_()
