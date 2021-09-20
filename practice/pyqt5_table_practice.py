import sys
from PyQt5.QtWidgets import *


class Tableclass(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.initUI()

        # QLineEdit 위젯 생성
        self.lineedit = QLineEdit(self)
        #self.lineedit.textChanged.connect(self.change_text)

        # Enter 클릭
        self.lineedit.returnPressed.connect(self.press_text)
        self.lineedit.setGeometry(10,10,200,30)

        # QLabel 설정
        self.label = QLabel(self)
        self.label.setGeometry(10,50,200,30)

        self.setGeometry(300, 100, 700, 300)
        self.show()

    def change_text(self, txt):
        self.label.setText(txt)
        self.label.adjustSize()

    def press_text(self):
        self.label.setText(self.lineedit.text())
        self.label.adjustSize()

    def initUI(self):
        a = self.tableWidget = QTableWidget()

        #행의 갯수 입력

        self.tableWidget.setRowCount(5)  # 행 개수 설정
        self.tableWidget.setColumnCount(4) #열 개수 설정


        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Tableclass()
    sys.exit(app.exec_())