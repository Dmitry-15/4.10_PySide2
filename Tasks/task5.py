#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtCore import QPropertyAnimation, QPoint

"""
B программе создается анимация круга, который движется от левой границы холста до правой. 
Изучите приведенную программу и самостоятельно запрограммируйте постепенное движение фигуры 
в ту точку холста, где пользователь кликает левой кнопкой мыши. Координаты события хранятся 
в его атрибутах x и y (event.x, event.y).
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Движение объекта по холсту")
        self.setGeometry(600, 460, 600, 460)
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color: purple;border-radius: 25%;")
        self.child.resize(50, 50)
        self.animation = QPropertyAnimation(self.child, b"pos")
        self.animation.setDuration(1500)

    def mousePressEvent(self, event):
        self.animation.setEndValue(QPoint(event.x() - 25, event.y() - 25))
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
