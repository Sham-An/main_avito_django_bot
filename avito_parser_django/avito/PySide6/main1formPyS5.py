
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

def button1_clicked():
    ui.slug_Scheme.setText("https://www.avito.ru")

app = QApplication([])
ui = loadUi("mainwindow.ui")
window = QMainWindow()
window.setWindowTitle("Task edit")
window.setCentralWidget(ui)

# Подключение функции button1_clicked к сигналу clicked кнопки button1
ui.button1.clicked.connect(button1_clicked)

window.show()
app.exec_()

# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
# from PyQt5.uic import loadUi
#
# # Создаем экземпляр приложения
# app = QApplication([])
#
# # Загружаем файл mainwindow.ui
# ui = loadUi("mainwindow.ui")
#
# # Создаем главное окно
# window = QMainWindow()
# window.setWindowTitle("My App")
#
# # Устанавливаем ui как центральный виджет главного окна
# window.setCentralWidget(ui)
#
# # Отображаем главное окно
# window.show()
#
# # Запускаем главный цикл приложения
# app.exec_()
