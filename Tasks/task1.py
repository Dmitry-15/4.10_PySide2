#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QWidget, QApplication, QListWidget, QPushButton, QAbstractItemView, QVBoxLayout, \
    QHBoxLayout

"""
Напишите программу, состоящую из двух списков Listbox. В первом будет, например, перечень товаров, 
заданный программно. Второй изначально пуст, пусть это будет перечень покупок. При клике на одну 
кнопку товар должен переходить из одного списка в другой. При клике на вторую кнопку – возвращаться 
(человек передумал покупать). Предусмотрите возможность множественного выбора элементов списка и их перемещения
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Список продуктов")
        self.setGeometry(400, 250, 400, 250)
        self.list1 = QListWidget()
        self.list1.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list2 = QListWidget()
        self.list2.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list1.addItems(products)
        self.button1 = QPushButton(">>>")
        self.button2 = QPushButton("<<<")
        self.button1.clicked.connect(self.add_item)
        self.button2.clicked.connect(self.del_item)

    def align(self):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        hbox.addWidget(self.list1)
        hbox.addLayout(vbox)
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        hbox.addWidget(self.list2)
        self.setLayout(hbox)

    def add_item(self):
        list_items = self.list1.selectedItems()
        for item in list_items:
            self.list1.takeItem(self.list1.row(item))
            self.list2.addItem(item)

    def del_item(self):
        list_items = self.list2.selectedItems()
        for item in list_items:
            self.list2.takeItem(self.list2.row(item))
            self.list1.addItem(item)


if __name__ == "__main__":
    products = ['apple', 'bananas', 'carrot', 'bread', 'butter', 'meat', 'potato', 'pineapple']
    app = QApplication(sys.argv)
    window = MainWindow()
    window.align()
    window.show()
    sys.exit(app.exec_())
