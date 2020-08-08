import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *



#ui 파일의 설정값을 가져오기 (한 세트로 만들기)
point_class = uic.loadUiType('project1/point.ui')[0]
pointcheck_class = uic.loadUiType('project1/pointCheck.ui')[0]
print(point_class)

# 포인트화면
class Point(QDialog,point_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_charity.clicked.connect(self.pointcheck_show)
        
    
    #포인트 완료 창을 띄우기
    def pointcheck_show(self):
        PointCheck.show()


#포인트 기부 완료 화면
class PointCheck_class(QDialog,pointcheck_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_charitycheck.clicked.connect(self.pointcheck_close)

    #확인 누르면 창이 닫힘.
    def pointcheck_close(self): 
        PointCheck.close()





if __name__ == "__main__":
#pyQt를 동작시켜주는 역할 
    app = QApplication(sys.argv) #시스템은 하나만 만들어 놓으면 된다.
#app2 = QApplication(sys.argv) #별도의 시스템
    Point = Point()
    Point.show() #메인UI 실행
    PointCheck = PointCheck_class()

#동작
app.exec_()
