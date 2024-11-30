import sys

from random import randint
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        diameter = randint(10, 150)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(50, 50, diameter, diameter)
        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
