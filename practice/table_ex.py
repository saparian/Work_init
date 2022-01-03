import sys, sqlite3
from PyQt5.QtWidgets import *

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
      self.setGeometry(300, 300, 500, 520)
      self.setWindowTitle("배합표 작성 폼")
      self.show()
   def run(self):
      self.cmd = "create table if not exists format (id integer PRIMARY KEY, name text NOT NULL);"
      self.cur.execute(self.cmd)
      self.conn.commit()
      print(self.cur.fetchall())
   
   def cleseEvent(self, QCloseEvent):
      print("close!")
      self.conn.close()
      
app = QApplication(sys.argv)
w = sql()
sys.exit(app.exec_())

      
      