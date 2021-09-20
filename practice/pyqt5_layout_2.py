# 우측정렬, 하단정렬 등 레이아웃 짜는 과정 (Layout_2)
# QHBoxLayout, QVBoxLayout 모듈 사용
# addStretch를 사용해서 정렬효과 적용

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        
        hbox = QHBoxLayout()
        hbox.addStretch(1) # 버튼이 차지하지 않고 있는 공간 만큼 늘어남, 빈공간 생성
        hbox.addWidget(okButton) # Stretch로 인해 버튼들이 오른쪽으로 붙어버림 (오른쪽 정렬효과)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1) # 버튼이 차지하지 않고 있는 공간 만큼 늘어남, 빈공간 생성
        vbox.addLayout(hbox) # Stretch로 인해 버튼들이 맨 아래로 붙음 (아래정렬 효과)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("Buttons")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())