import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton("Table_1", self)

        a = self.tableWidget = QTableWidget() # Table 생성
        self.tableWidget.setRowCount(20) # Table 행의 수
        self.tableWidget.setColumnCount(4) # Table 열의 수
        

        #self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers) # 편집 불가능
        #self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked) # 더블클릭시 편집가능
        self.tableWidget.setEditTriggers(QAbstractItemView.AnyKeyPressed) # 키가 입력됐을때 편집
        
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for i in range(20):
            for j in range(4):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(i+j)))

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.setWindowTitle("table")
        self.setGeometry(300, 100, 600, 400)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

