import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget

# Qwidget 상속 받아서 사용하기 
# (객체지향 : class 및 data 필요)
class Exam(QWidget):
    def __init__(self): #클래스가 생성될 때 자동으로 실행되는 함수
        super().__init__() # 상위객체 설정
        self.initUI()
    def initUI(self):
        btn = QPushButton('dkanrjdk', self)
        btn.resize(btn.sizeHint())
        btn.setToolTip('툴팁입니다.<b>툴팁입니다')
        btn.move(20, 30)

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('첫번째 학습시간')
        self.show()

app = QApplication(sys.argv) # 모든 application 오브젝트를 필요로함
w = Exam()
sys.exit(app.exec_())  # 프로그램을 종료하게 하기 위해서 있음 
# app.exec_() 이벤트 처리를 위한 메인루프를 실행
# app.exec_() 가 끝나면 exit가 실행되서 종료됨
