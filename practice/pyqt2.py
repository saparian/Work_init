import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication #이벤트 처리에 대한 것을 담당

class Exam(QWidget): # 클래스란 객체를 만들어내는 공장이라 이해할 수 있음
    def __init__(self): # 클래스가 생성될 때 자동으로 생성되는 함수
        super().__init__()
        self.initUI()
    def initUI(self):
        btn = QPushButton("push me!", self)
        btn.resize(btn.sizeHint()) # 버튼 사이즈
        btn.move(50, 50) # 버튼 위치
        btn.clicked.connect(QCoreApplication.instance().quit) # instance 생성한 후 Quit 와 clicked라는 시그널을 연결


        self.resize(500, 500) # resize 했을때 정 가운데 창이 뜸, (x축, y축)
        self.setWindowTitle("두 번째 시간")        
        self.show()

    def closeEvent(self, QCloseEvent): # 종료할 때 어떻게 할지
        ans = QMessageBox.question(self, "종료 확인", "종료하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes) # 종료확인 메시지 박스 (객체, Title, 메시지, 버튼.메시지, 기본값)

        if ans == QMessageBox.Yes:
            QCloseEvent.accept() # 종료이벤트 승인
        else:
            QCloseEvent.ignore() # 종료이벤트 무시



app = QApplication(sys.argv)
w = Exam() # 클래스를 호출해서 "w"라는 객체를 만들어냄
sys.exit(app.exec_())