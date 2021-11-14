import random
import sys

from PyQt5 import uic, QtCore
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Кружочки')
        self.circle_button.clicked.connect(self.run)
        self.is_paint = False

    def run(self):
        self.is_paint = True
        self.update()

    def paintEvent(self, event) -> None:
        qp = QPainter()
        qp.begin(self)
        self.draw_random_ellipses(qp)
        qp.end()

    def draw_random_ellipses(self, qp):
        try:
            if self.is_paint:
                print('asdasd')
                qp.setBrush(QColor(255, 255, 0))
                radius = random.randint(50, 200)
                x, y = random.randint(0, 600), random.randint(0, 600)
                qp.drawEllipse(x, y, radius, radius)
                self.is_paint = False
        except Exception as e:
            print(e.__repr__())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
