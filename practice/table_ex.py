# PYqt5 19번째 강의 (https://youtu.be/YO6fmMfdZDw)

import sys, sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTreeView
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import Qt

class sql(QWidget):
   def __init__(self):
      super().__init__()
      self.sqlConnect()
      self.initUI()
      self.run()
      
   def sqlConnect(self):
      try:
         self.conn = sqlite3.connect('form.db')
      except:
         print("문제가 있네요!")   
         exit(1)
      print("연결 성공!")
      self.cur = self.conn.cursor()
   def initUI(self):
      self.w = 400
      self.h = 420
      self.btnSize = 40 # 버튼 사이즈
      self.setGeometry(300, 300, self.w, self.h)
      self.setWindowTitle("배합표 작성 폼")
            
      self.lbl번호 = QLabel("번호", self)
      self.lbl번호.move(25, 25)
      self.txt번호 = QLineEdit(self)
      self.txt번호.move(25 + 49, 22)
      self.lbl이름 = QLabel("이름", self)
      self.lbl이름.move(25, 60)
      self.txt이름 = QLineEdit(self)
      self.txt이름.move(25 + 49, 57)
      self.lbl주소 = QLabel("주소", self)
      self.lbl주소.move(25, 95)
      self.txt주소 = QLineEdit(self)
      self.txt주소.move(25 + 49, 92)
      
      # TreeView
      self.리스트 = QTreeView(self)
      self.리스트.setRootIsDecorated(False)     # 행 앞부분에 빈 공간 제거하기 위한 코드
      #self.리스트.setRootIsDecorated(True)     # 행 앞부분에 빈공간 있음
      self.리스트.setAlternatingRowColors(True)
      self.리스트.resize(330, 200)
      self.리스트.move(25, 130)
      
      self.내용 = QStandardItemModel(0, 3, self)  # (행 개수, 열 개수, self)
      self.내용.setHeaderData(0, Qt.Horizontal, "번호") # 헤더 방향이 가로이기때문에 Horizontal 사용
      self.내용.setHeaderData(1, Qt.Horizontal, "이름")
      self.내용.setHeaderData(2, Qt.Horizontal, "주소")
      
      self.내용.insertRows(self.내용.rowCount(), 1) # 트리뷰에 행 추가
      self.내용.setData(self.내용.index(0, 0), self.내용.rowCount())
      self.내용.setData(self.내용.index(0, 1), "홍길동")
      self.내용.setData(self.내용.index(0, 2), "인천시")

      self.내용.insertRows(self.내용.rowCount(), 1) # 트리뷰에 행 추가
      self.내용.setData(self.내용.index(1, 0), self.내용.rowCount())
      self.내용.setData(self.내용.index(1, 1), "장동건")
      self.내용.setData(self.내용.index(1, 2), "서울시")
      
      self.리스트.setModel(self.내용)
      self.리스트.setColumnWidth(0, 40)
      self.리스트.setColumnWidth(1, 80)
      # 버튼 생성
      self.cmd이전 = QPushButton("이전", self)
      self.cmd이전.resize(self.btnSize, self.btnSize)
      self.cmd다음 = QPushButton("다음", self)
      self.cmd다음.resize(self.btnSize, self.btnSize)
      self.cmd신규 = QPushButton("신규", self)
      self.cmd신규.resize(self.btnSize, self.btnSize)
      self.cmd수정 = QPushButton("수정", self)
      self.cmd수정.resize(self.btnSize, self.btnSize)
      self.cmd삭제 = QPushButton("삭제", self)
      self.cmd삭제.resize(self.btnSize, self.btnSize)
      
      self.show()
      
   def run(self):
      self.cmd = ""
      self.cur.execute(self.cmd)
      self.conn.commit()
      print(self.cur.fetchall())
   
   # 버튼 리사이징 : 창 크기 조절에도 버튼 위치가 일정하게 배열될 수 있도록 함
   def resizeEvent(self, QResizeEvent):
          self.btnX = self.width() - 220
          self.btnY = self.height() - 60
          
          self.cmd이전.move(self.btnX, self.btnY)
          self.cmd다음.move(self.btnX + self.btnSize*1, self.btnY)
          self.cmd신규.move(self.btnX + self.btnSize*2, self.btnY)
          self.cmd수정.move(self.btnX + self.btnSize*3, self.btnY)
          self.cmd삭제.move(self.btnX + self.btnSize*4, self.btnY)
   
   def cleseEvent(self, QCloseEvent):
      print("close!")
      self.conn.close()
      
app = QApplication(sys.argv)
w = sql()
sys.exit(app.exec_())

      
      