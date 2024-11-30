import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("UI.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())