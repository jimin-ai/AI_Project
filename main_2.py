from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from main_1 import Ui_dialog
import sys
 


#메인페이지에서 위에 버튼 누르면 바뀌는 클래스
class btnTop_class(QMainWindow, Ui_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_main.clicked.connect(self.set_funcFrame)
        self.btn_app.clicked.connect(self.set_funcFrame)
        self.btn_result.clicked.connect(self.set_funcFrame)
        self.btn_my.clicked.connect(self.set_funcFrame)
        self.btn_point.clicked.connect(self.set_funcFrame)
        
        # self.show()
 
    def set_funcFrame(self):
        btn_c = self.sender()
        if btn_c.isChecked():
            print(btn_c.objectName(),"is checked")
            if btn_c.objectName() == "btn_main":
                self.btn_app.setChecked(False)
                self.btn_result.setChecked(False)
                self.btn_my.setChecked(False)
                self.btn_point.setChecked(False)
                self.stackedWidget.setCurrentIndex(0)
            elif btn_c.objectName() == "btn_app":
                self.btn_main.setChecked(False)
                self.btn_result.setChecked(False)
                self.btn_my.setChecked(False)
                self.btn_point.setChecked(False)
                self.stackedWidget.setCurrentIndex(1)
            elif btn_c.objectName() == ".btn_result":
                self.btn_main.setChecked(False)
                self.btn_app.setChecked(False)
                self.btn_my.setChecked(False)
                self.btn_point.setChecked(False)
                self.stackedWidget.setCurrentIndex(2)
            elif btn_c.objectName() == "btn_my":
                self.btn_main.setChecked(False)
                self.btn_app.setChecked(False)
                self.btn_result.setChecked(False)
                self.btn_point.setChecked(False)
                self.stackedWidget.setCurrentIndex(3)
            else:
                self.btn_main.setChecked(False)
                self.btn_app.setChecked(False)
                self.btn_result.setChecked(False)
                self.btn_my.setChecked(False)
                self.stackedWidget.setCurrentIndex(4)
        else:
            btn_c.setChecked(True)
 
 
app = QApplication([])
# BtnTop = btnTop_class()
sys.exit(app.exec_())