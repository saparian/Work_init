# 절대 좌표로 레이아웃 짜는 과정 (Layout_1)

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lb11 = QLabel("Zetcode", self)
        lb11.move(15,10)

        lb12 = QLabel("tutorials", self)
        lb12.move(35, 40)

        lb13 = QLabel("for programmers", self)
        lb13.move(55, 70)

        self.setGeometry(300, 300, 1050, 150)
        self.setWindowTitle("Absolute")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


