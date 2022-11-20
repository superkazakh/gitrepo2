import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('balls.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.setFixedSize(self.size())
        self.circ = False

    def run(self):
        self.circ = True
        self.repaint()

    def draw_circle(self):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor('yellow'))
        for i in range(40):
            h = random.randrange(1, 150)
            qp.drawEllipse(random.randint(0, self.x()), random.randint(0, self.y()),
                           h, h)
        qp.end()

    def paintEvent(self, event):
        if self.circ is True:
            self.draw_circle()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
