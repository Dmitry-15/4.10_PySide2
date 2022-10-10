#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QApplication, QWidget, QLineEdit,  QVBoxLayout, QListWidget

"""
Напишите программу по следующему описанию. Нажатие Enter в однострочном текстовом поле 
приводит к перемещению текста из него в список. При двойном клике по элементу-строке 
списка, она должна копироваться в текстовое поле.
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Перемещение текста")
        self.setGeometry(400, 250, 400, 250)
        self.list = QListWidget()
        self.list.itemDoubleClicked.connect(self.copy_item)
        self.line_edit = QLineEdit()
        self.line_edit.returnPressed.connect(self.add_item)

    def align(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.line_edit)
        vbox.addWidget(self.list)
        self.setLayout(vbox)

    def add_item(self):
        self.list.addItem(self.line_edit.text())
        self.line_edit.clear()

    def copy_item(self):
        list_items = self.list.selectedItems()
        if not list_items:
            return
        for item in list_items:
            self.line_edit.setText(item.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.align()
    window.show()
    sys.exit(app.exec_())
