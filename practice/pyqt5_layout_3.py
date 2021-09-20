# 그리드 형태로 레이아웃 짜기 (layout_3)
# QGridLayout 모듈 사용

import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout() # 변수를 grid 형태로 설정
        self.setLayout(grid) # 레이아웃을 변수에 설정된 형태(grid)로 설정

        names = ['cls', 'Bck', '', 'Close',
                '7', '8', '9', '/', 
                '4', '5', '6', '*',
                '1', '2', '3', '-', 
                '0', '.', '=', '+' ]

        # 튜플형태로 리스트에 저장
        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position) 
            # '*'의 사용은 튜플값을 추출해서 넘겨줌
            # (0,1) -> 0,1
        
        self.move(300, 150)
        self.setWindowTitle('calculator')
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
