#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QTextEdit

"""
Напишите программу по описанию. Размеры многострочного текстового поля определяются 
значениями, введенными в однострочные текстовые поля. Изменение размера происходит 
при нажатии мышью на кнопку, а также при нажатии клавиши Enter. Цвет фона экземпляра 
Text светлосерый (lightgrey), когда поле не в фокусе, и белый, когда имеет фокус.
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        QApplication.instance().focusChanged.connect(self.focus_change)
        self.setWindowTitle("Изменение размера поля")
        self.setGeometry(400, 250, 400, 250)
        self.line_edit1 = QLineEdit()
        self.line_edit2 = QLineEdit()
        self.line_edit2.returnPressed.connect(self.change_size)
        self.text_edit = QTextEdit()
        self.button1 = QPushButton("Изменить")
        self.button1.clicked.connect(self.change_size)

    def align(self):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        hbox.addWidget(self.line_edit1)
        hbox.addWidget(self.line_edit2)
        hbox.addWidget(self.button1)
        vbox.addLayout(hbox)
        vbox.addWidget(self.text_edit)
        self.setLayout(vbox)

    def change_size(self):
        self.text_edit.resize(int(self.line_edit1.text()), int(self.line_edit2.text()))

    def focus_change(self, focus, unfocus):
        if self.text_edit == focus:
            self.text_edit.setStyleSheet(f"background-color: #fff;")
        elif self.text_edit == unfocus:
            self.text_edit.setStyleSheet(f"background-color: #d3d3d3;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.align()
    window.show()
    sys.exit(app.exec_())
