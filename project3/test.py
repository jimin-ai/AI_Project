import  sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd


test_ui = uic.loadUiType("project3/test.ui")[0]

class Test_Ui(QDialog,test_ui):
    # 기본값 입력
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.testclick)


    def testclick(self):
        text=self.comboBox.currentText()
        if text == "냉장고":
            text="AC"
        elif text == "티비":
            text ="TV"
        elif text == "세탁기":
            text = "WS"

        self.lbltext.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Test=Test_Ui()
    Test.show()

    app.exec_()