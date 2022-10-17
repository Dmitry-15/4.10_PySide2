#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random
from PySide2.QtCore import Qt, QPoint
from PySide2.QtGui import QPainter, QPolygon, QBrush, QPen
from PySide2.QtWidgets import QApplication, QWidget

"""
Создайте на холсте изображение дома с травой и солнцем.
"""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # Вызываем конструктор базового класса QWidget
        self.setWindowTitle("Рисунок")
        self.setGeometry(600, 460, 600, 460)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 6, Qt.SolidLine))
        painter.setBrush(Qt.red)
        painter.drawRect(287, 167, 278, 270)
        painter.setPen(QPen(Qt.black, 8, Qt.SolidLine))
        painter.setBrush((QBrush(Qt.cyan)))
        painter.drawRect(369, 225, 115, 68)
        painter.drawLine(428, 292, 428, 225)
        painter.drawLine(370, 259, 482, 259)
        painter.setBrush((QBrush(Qt.black)))
        painter.drawRect(399, 321, 58, 104)
        painter.setBrush((QBrush(Qt.white)))
        painter.drawEllipse(436, 364, 20, 20)
        painter.setBrush((QBrush(Qt.blue)))
        points = QPolygon([QPoint(260, 166), QPoint(433, 36), QPoint(589, 166)])
        painter.drawPolygon(points)
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        painter.drawEllipse(33, 24, 100, 100)
        painter.drawLine(129, 52, 201, 22)
        painter.drawLine(134, 83, 192, 87)
        painter.drawLine(118, 111, 178, 154)
        painter.drawLine(96, 123, 94, 165)
        painter.drawLine(56, 116, 20, 163)
        painter.drawLine(34, 85, 15, 97)
        painter.drawLine(45, 40, 25, 17)
        painter.drawLine(105, 30, 110, 5)
        self.grass(painter)
        self.dog(painter)

    def dog(self, painter):
        painter.begin(self)
        points1 = QPolygon([QPoint(152, 415), QPoint(181, 395), QPoint(181, 416)])
        points2 = QPolygon([QPoint(152, 415), QPoint(121, 381), QPoint(87, 415)])
        points3 = QPolygon([QPoint(97, 404), QPoint(122, 382), QPoint(97, 355)])
        points4 = QPolygon([QPoint(97, 353), QPoint(123, 327), QPoint(97, 300)])
        points5 = QPolygon([QPoint(97, 353), QPoint(72, 327), QPoint(97, 300)])
        points6 = QPolygon([QPoint(130, 330), QPoint(130, 300), QPoint(106, 305)])
        points7 = QPolygon([QPoint(66, 330), QPoint(66, 300), QPoint(88, 305)])
        points8 = QPolygon([QPoint(97, 340), QPoint(100, 335), QPoint(94, 335)])
        painter.setPen(QPen(Qt.black))
        painter.setBrush(QBrush(Qt.yellow))
        painter.drawPolygon(points1)
        painter.drawPolygon(points2)
        painter.drawPolygon(points3)
        painter.drawPolygon(points4)
        painter.drawPolygon(points5)
        painter.drawPolygon(points6)
        painter.drawPolygon(points7)
        painter.setBrush((QBrush(Qt.black)))
        painter.drawPolygon(points8)
        painter.setBrush(QBrush(Qt.black))
        painter.drawEllipse(86, 318, 8, 10)
        painter.drawEllipse(100, 318, 8, 10)

    def grass(self, painter):
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.green, 2, Qt.SolidLine))
        painter.setBrush(Qt.darkGreen)
        for i in range(30):
            painter.drawArc(
                random.randint(1, 10),
                300,
                i * 40,
                400,
                0 * 250,
                random.randint(45, 85) * 8,
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
