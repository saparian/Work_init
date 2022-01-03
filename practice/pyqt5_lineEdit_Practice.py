
import sys
from PyQt5.QtWidgets import *

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        title = QLabel("원료")
        titleEdit = QLineEdit()
        titlebtn = QPushButton('입력', self)

        ########
        titlebtn.returnPressed.connect(titleEdit)
        ########


        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1,)
        grid.addWidget(titlebtn, 1, 2)

        self.setLayout(grid)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('ATbio')
        self.show()

    #######
    def press_text(self):
        self.label.setText(titleEdit)
        self.label.adjustSize()
    #######

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
