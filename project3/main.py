# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SMT022\Desktop\ddddd\project3\main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(1070, 776)
        self.stackedWidget = QtWidgets.QStackedWidget(dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(80, 140, 911, 591))
        self.stackedWidget.setObjectName("stackedWidget")
        self.stack_main = QtWidgets.QWidget()
        self.stack_main.setObjectName("stack_main")
        self.main_lbl = QtWidgets.QLabel(self.stack_main)
        self.main_lbl.setGeometry(QtCore.QRect(30, 20, 201, 81))
        self.main_lbl.setObjectName("main_lbl")
        self.main_txt = QtWidgets.QTextBrowser(self.stack_main)
        self.main_txt.setGeometry(QtCore.QRect(50, 110, 256, 192))
        self.main_txt.setObjectName("main_txt")
        self.stackedWidget.addWidget(self.stack_main)
        self.stack_app = QtWidgets.QWidget()
        self.stack_app.setObjectName("stack_app")
        self.app_lbl = QtWidgets.QLabel(self.stack_app)
        self.app_lbl.setGeometry(QtCore.QRect(30, 20, 131, 61))
        self.app_lbl.setObjectName("app_lbl")
        self.app_combo_type = QtWidgets.QComboBox(self.stack_app)
        self.app_combo_type.setGeometry(QtCore.QRect(40, 90, 91, 31))
        self.app_combo_type.setObjectName("app_combo_type")
        self.app_combo_type.addItem("")
        self.app_combo_type.addItem("")
        self.app_combo_type.addItem("")
        self.app_combo_type.addItem("")
        self.app_combo_type.addItem("")
        self.app_combo_type.addItem("")
        self.app_combo_type.addItem("")
        self.app_lineedit_search = QtWidgets.QLineEdit(self.stack_app)
        self.app_lineedit_search.setGeometry(QtCore.QRect(160, 90, 191, 31))
        self.app_lineedit_search.setObjectName("app_lineedit_search")
        self.app_btn_search = QtWidgets.QPushButton(self.stack_app)
        self.app_btn_search.setGeometry(QtCore.QRect(370, 90, 91, 31))
        self.app_btn_search.setObjectName("app_btn_search")
        self.app_lbl_direct = QtWidgets.QLabel(self.stack_app)
        self.app_lbl_direct.setGeometry(QtCore.QRect(40, 480, 131, 31))
        self.app_lbl_direct.setObjectName("app_lbl_direct")
        self.app_lineedit_model = QtWidgets.QLineEdit(self.stack_app)
        self.app_lineedit_model.setGeometry(QtCore.QRect(40, 530, 141, 31))
        self.app_lineedit_model.setObjectName("app_lineedit_model")
        self.app_lineedit_power = QtWidgets.QLineEdit(self.stack_app)
        self.app_lineedit_power.setGeometry(QtCore.QRect(210, 530, 131, 31))
        self.app_lineedit_power.setObjectName("app_lineedit_power")
        self.app_btn_direct_register = QtWidgets.QPushButton(self.stack_app)
        self.app_btn_direct_register.setGeometry(QtCore.QRect(700, 530, 91, 31))
        self.app_btn_direct_register.setObjectName("app_btn_direct_register")
        self.app_lineedit_hour = QtWidgets.QLineEdit(self.stack_app)
        self.app_lineedit_hour.setGeometry(QtCore.QRect(40, 430, 131, 31))
        self.app_lineedit_hour.setObjectName("app_lineedit_hour")
        self.app_btn_register = QtWidgets.QPushButton(self.stack_app)
        self.app_btn_register.setGeometry(QtCore.QRect(210, 440, 71, 21))
        self.app_btn_register.setObjectName("app_btn_register")
        self.app_lineedit_size = QtWidgets.QLineEdit(self.stack_app)
        self.app_lineedit_size.setGeometry(QtCore.QRect(480, 530, 81, 31))
        self.app_lineedit_size.setObjectName("app_lineedit_size")
        self.app_lineedit_direct_hour = QtWidgets.QLineEdit(self.stack_app)
        self.app_lineedit_direct_hour.setGeometry(QtCore.QRect(370, 530, 81, 31))
        self.app_lineedit_direct_hour.setObjectName("app_lineedit_direct_hour")
        self.app_combo_efficiency = QtWidgets.QComboBox(self.stack_app)
        self.app_combo_efficiency.setGeometry(QtCore.QRect(590, 530, 81, 31))
        self.app_combo_efficiency.setObjectName("app_combo_efficiency")
        self.app_combo_efficiency.addItem("")
        self.app_combo_efficiency.addItem("")
        self.app_combo_efficiency.addItem("")
        self.app_combo_efficiency.addItem("")
        self.app_combo_efficiency.addItem("")
        self.label_10 = QtWidgets.QLabel(self.stack_app)
        self.label_10.setGeometry(QtCore.QRect(590, 500, 101, 16))
        self.label_10.setObjectName("label_10")
        self.app_model_search = QtWidgets.QTableWidget(self.stack_app)
        self.app_model_search.setGeometry(QtCore.QRect(40, 140, 621, 181))
        self.app_model_search.setObjectName("app_model_search")
        self.app_model_search.setColumnCount(6)
        self.app_model_search.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.app_model_search.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.app_model_search.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.app_model_search.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.app_model_search.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.app_model_search.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.app_model_search.setHorizontalHeaderItem(5, item)
        self.stackedWidget.addWidget(self.stack_app)
        self.stack_result = QtWidgets.QWidget()
        self.stack_result.setObjectName("stack_result")
        self.result_lbl = QtWidgets.QLabel(self.stack_result)
        self.result_lbl.setGeometry(QtCore.QRect(50, 0, 141, 41))
        self.result_lbl.setObjectName("result_lbl")
        self.result_tab_visulal = QtWidgets.QTabWidget(self.stack_result)
        self.result_tab_visulal.setGeometry(QtCore.QRect(620, 100, 261, 341))
        self.result_tab_visulal.setObjectName("result_tab_visulal")
        self.day = QtWidgets.QWidget()
        self.day.setObjectName("day")
        self.result_tab_visulal.addTab(self.day, "")
        self.month = QtWidgets.QWidget()
        self.month.setObjectName("month")
        self.result_tab_visulal.addTab(self.month, "")
        self.result_lbl_visual = QtWidgets.QLabel(self.stack_result)
        self.result_lbl_visual.setGeometry(QtCore.QRect(650, 40, 191, 21))
        self.result_lbl_visual.setObjectName("result_lbl_visual")
        self.result_table_power = QtWidgets.QTableWidget(self.stack_result)
        self.result_table_power.setGeometry(QtCore.QRect(50, 110, 421, 181))
        self.result_table_power.setObjectName("result_table_power")
        self.result_table_power.setColumnCount(0)
        self.result_table_power.setRowCount(0)
        self.result_lbl_recommend = QtWidgets.QLabel(self.stack_result)
        self.result_lbl_recommend.setGeometry(QtCore.QRect(30, 290, 271, 31))
        self.result_lbl_recommend.setObjectName("result_lbl_recommend")
        self.result_table_recommend = QtWidgets.QTableWidget(self.stack_result)
        self.result_table_recommend.setGeometry(QtCore.QRect(30, 390, 551, 181))
        self.result_table_recommend.setObjectName("result_table_recommend")
        self.result_table_recommend.setColumnCount(5)
        self.result_table_recommend.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.result_table_recommend.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table_recommend.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table_recommend.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table_recommend.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table_recommend.setHorizontalHeaderItem(4, item)
        self.result_lbl_power = QtWidgets.QLabel(self.stack_result)
        self.result_lbl_power.setGeometry(QtCore.QRect(50, 60, 341, 31))
        self.result_lbl_power.setObjectName("result_lbl_power")
        self.radioButton_5 = QtWidgets.QRadioButton(self.stack_result)
        self.radioButton_5.setGeometry(QtCore.QRect(40, 360, 90, 16))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_2 = QtWidgets.QRadioButton(self.stack_result)
        self.radioButton_2.setGeometry(QtCore.QRect(140, 330, 90, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.stack_result)
        self.radioButton_3.setGeometry(QtCore.QRect(240, 330, 90, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_6 = QtWidgets.QRadioButton(self.stack_result)
        self.radioButton_6.setGeometry(QtCore.QRect(140, 360, 90, 16))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.stack_result)
        self.radioButton_7.setGeometry(QtCore.QRect(240, 360, 90, 16))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_1 = QtWidgets.QRadioButton(self.stack_result)
        self.radioButton_1.setGeometry(QtCore.QRect(40, 330, 90, 16))
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_4 = QtWidgets.QRadioButton(self.stack_result)
        self.radioButton_4.setGeometry(QtCore.QRect(340, 330, 90, 16))
        self.radioButton_4.setObjectName("radioButton_4")
        self.stackedWidget.addWidget(self.stack_result)
        self.stack_my = QtWidgets.QWidget()
        self.stack_my.setObjectName("stack_my")
        self.my_lbl = QtWidgets.QLabel(self.stack_my)
        self.my_lbl.setGeometry(QtCore.QRect(20, 20, 191, 61))
        self.my_lbl.setObjectName("my_lbl")
        self.my_lbl_app = QtWidgets.QLabel(self.stack_my)
        self.my_lbl_app.setGeometry(QtCore.QRect(40, 80, 151, 31))
        self.my_lbl_app.setObjectName("my_lbl_app")
        self.my_table_app = QtWidgets.QTableWidget(self.stack_my)
        self.my_table_app.setGeometry(QtCore.QRect(40, 120, 501, 192))
        self.my_table_app.setObjectName("my_table_app")
        self.my_table_app.setColumnCount(0)
        self.my_table_app.setRowCount(0)
        self.my_txt_ = QtWidgets.QTextBrowser(self.stack_my)
        self.my_txt_.setGeometry(QtCore.QRect(610, 230, 241, 231))
        self.my_txt_.setObjectName("my_txt_")
        self.my_table_graph = QtWidgets.QTextBrowser(self.stack_my)
        self.my_table_graph.setGeometry(QtCore.QRect(40, 350, 501, 192))
        self.my_table_graph.setObjectName("my_table_graph")
        self.my_btn_update = QtWidgets.QPushButton(self.stack_my)
        self.my_btn_update.setGeometry(QtCore.QRect(660, 20, 101, 21))
        self.my_btn_update.setObjectName("my_btn_update")
        self.my_btn_delete = QtWidgets.QPushButton(self.stack_my)
        self.my_btn_delete.setGeometry(QtCore.QRect(780, 20, 101, 21))
        self.my_btn_delete.setObjectName("my_btn_delete")
        self.my_txt_point = QtWidgets.QTextBrowser(self.stack_my)
        self.my_txt_point.setGeometry(QtCore.QRect(610, 120, 241, 81))
        self.my_txt_point.setObjectName("my_txt_point")
        self.stackedWidget.addWidget(self.stack_my)
        self.stack_point = QtWidgets.QWidget()
        self.stack_point.setObjectName("stack_point")
        self.point_lbl = QtWidgets.QLabel(self.stack_point)
        self.point_lbl.setGeometry(QtCore.QRect(20, 20, 161, 51))
        self.point_lbl.setObjectName("point_lbl")
        self.point_table = QtWidgets.QTableWidget(self.stack_point)
        self.point_table.setGeometry(QtCore.QRect(20, 70, 411, 171))
        self.point_table.setObjectName("point_table")
        self.point_table.setColumnCount(4)
        self.point_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.point_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.point_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.point_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.point_table.setHorizontalHeaderItem(3, item)
        self.point_btn_charity = QtWidgets.QPushButton(self.stack_point)
        self.point_btn_charity.setGeometry(QtCore.QRect(310, 260, 121, 31))
        self.point_btn_charity.setObjectName("point_btn_charity")
        self.point_btn__use = QtWidgets.QPushButton(self.stack_point)
        self.point_btn__use.setGeometry(QtCore.QRect(160, 260, 121, 31))
        self.point_btn__use.setObjectName("point_btn__use")
        self.point_txt = QtWidgets.QTextBrowser(self.stack_point)
        self.point_txt.setGeometry(QtCore.QRect(30, 340, 551, 192))
        self.point_txt.setObjectName("point_txt")
        self.stackedWidget.addWidget(self.stack_point)
        self.btn_my = QtWidgets.QPushButton(dialog)
        self.btn_my.setGeometry(QtCore.QRect(670, 30, 141, 81))
        self.btn_my.setCheckable(True)
        self.btn_my.setObjectName("btn_my")
        self.btn_main = QtWidgets.QPushButton(dialog)
        self.btn_main.setGeometry(QtCore.QRect(90, 30, 141, 81))
        self.btn_main.setCheckable(True)
        self.btn_main.setObjectName("btn_main")
        self.btn_result = QtWidgets.QPushButton(dialog)
        self.btn_result.setGeometry(QtCore.QRect(470, 30, 141, 81))
        self.btn_result.setCheckable(True)
        self.btn_result.setObjectName("btn_result")
        self.btn_point = QtWidgets.QPushButton(dialog)
        self.btn_point.setGeometry(QtCore.QRect(870, 30, 141, 81))
        self.btn_point.setCheckable(True)
        self.btn_point.setObjectName("btn_point")
        self.btn_app = QtWidgets.QPushButton(dialog)
        self.btn_app.setGeometry(QtCore.QRect(280, 30, 141, 81))
        self.btn_app.setCheckable(True)
        self.btn_app.setObjectName("btn_app")
        self.btn_main.raise_()
        self.stackedWidget.raise_()
        self.btn_my.raise_()
        self.btn_result.raise_()
        self.btn_point.raise_()
        self.btn_app.raise_()

        self.retranslateUi(dialog)
        self.stackedWidget.setCurrentIndex(1)
        self.result_tab_visulal.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dialog"))
        self.main_lbl.setText(_translate("dialog", "main 페이지 입니다"))
        self.main_txt.setHtml(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">프로그램 소개</p></body></html>"))
        self.app_lbl.setText(_translate("dialog", "제품등록"))
        self.app_combo_type.setItemText(0, _translate("dialog", "청소기"))
        self.app_combo_type.setItemText(1, _translate("dialog", "전자렌지"))
        self.app_combo_type.setItemText(2, _translate("dialog", "전기밥솥"))
        self.app_combo_type.setItemText(3, _translate("dialog", "에어컨"))
        self.app_combo_type.setItemText(4, _translate("dialog", "세탁기"))
        self.app_combo_type.setItemText(5, _translate("dialog", "tv"))
        self.app_combo_type.setItemText(6, _translate("dialog", "냉장고"))
        self.app_lineedit_search.setText(_translate("dialog", "모델명 검색"))
        self.app_btn_search.setText(_translate("dialog", "검색"))
        self.app_lbl_direct.setText(_translate("dialog", "직접등록"))
        self.app_lineedit_model.setText(_translate("dialog", "모델명"))
        self.app_lineedit_power.setText(_translate("dialog", "소비전력"))
        self.app_btn_direct_register.setText(_translate("dialog", "등록"))
        self.app_lineedit_hour.setText(_translate("dialog", "사용시간"))
        self.app_btn_register.setText(_translate("dialog", "등록"))
        self.app_lineedit_size.setText(_translate("dialog", "용량"))
        self.app_lineedit_direct_hour.setText(_translate("dialog", "사용시간"))
        self.app_combo_efficiency.setItemText(0, _translate("dialog", "1"))
        self.app_combo_efficiency.setItemText(1, _translate("dialog", "2"))
        self.app_combo_efficiency.setItemText(2, _translate("dialog", "3"))
        self.app_combo_efficiency.setItemText(3, _translate("dialog", "4"))
        self.app_combo_efficiency.setItemText(4, _translate("dialog", "5"))
        self.label_10.setText(_translate("dialog", "에너지효율등급"))
        item = self.app_model_search.horizontalHeaderItem(0)
        item.setText(_translate("dialog", "모델명"))
        item = self.app_model_search.horizontalHeaderItem(1)
        item.setText(_translate("dialog", "소비전력"))
        item = self.app_model_search.horizontalHeaderItem(2)
        item.setText(_translate("dialog", "용량"))
        item = self.app_model_search.horizontalHeaderItem(3)
        item.setText(_translate("dialog", "등급"))
        item = self.app_model_search.horizontalHeaderItem(4)
        item.setText(_translate("dialog", "탄소인증"))
        self.result_lbl.setText(_translate("dialog", "결과 페이지"))
        self.result_tab_visulal.setTabText(self.result_tab_visulal.indexOf(self.day), _translate("dialog", "day"))
        self.result_tab_visulal.setTabText(self.result_tab_visulal.indexOf(self.month), _translate("dialog", "month"))
        self.result_lbl_visual.setText(_translate("dialog", "일별 월별 사용 동적시각화"))
        self.result_lbl_recommend.setText(_translate("dialog", "추천 제품 5개/ 탄소발자국 인증 제품 5개"))
        item = self.result_table_recommend.horizontalHeaderItem(0)
        item.setText(_translate("dialog", "모델명"))
        item = self.result_table_recommend.horizontalHeaderItem(1)
        item.setText(_translate("dialog", "소비전력"))
        item = self.result_table_recommend.horizontalHeaderItem(2)
        item.setText(_translate("dialog", "용량"))
        item = self.result_table_recommend.horizontalHeaderItem(3)
        item.setText(_translate("dialog", "등급"))
        item = self.result_table_recommend.horizontalHeaderItem(4)
        item.setText(_translate("dialog", "탄소인증제품"))
        self.result_lbl_power.setText(_translate("dialog", "보유제품 소비전력&소비전력 높은 제품 행 색깔 바꿔 알려주기"))
        self.radioButton_5.setText(_translate("dialog", "세탁기"))
        self.radioButton_2.setText(_translate("dialog", "전자렌지"))
        self.radioButton_3.setText(_translate("dialog", "전기밥솥"))
        self.radioButton_6.setText(_translate("dialog", "tv"))
        self.radioButton_7.setText(_translate("dialog", "냉장고"))
        self.radioButton_1.setText(_translate("dialog", "청소기"))
        self.radioButton_4.setText(_translate("dialog", "에어컨"))
        self.my_lbl.setText(_translate("dialog", "마이페이지"))
        self.my_lbl_app.setText(_translate("dialog", "가전 제품 보유내역"))
        self.my_txt_.setHtml(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">회원의 전기 사용량에 대한 설명</p></body></html>"))
        self.my_table_graph.setHtml(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">에너지 사용 세부 조회- <span style=\" font-family:\'맑은 고딕\';\">에너지 사용량을 일별, 월별, 분기별로 원형그래프를 이용하여 전체 에너지 사용량 대비 각 부분의 소비 비율을 파악할 수 있도록 하며, 수치를 기재 하여 세부 데이터를 확인할 수 있도록 함.</span></p></body></html>"))
        self.my_btn_update.setText(_translate("dialog", "개인정보 수정"))
        self.my_btn_delete.setText(_translate("dialog", "회원탈퇴"))
        self.my_txt_point.setHtml(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'맑은 고딕\';\">포인트 적립/사용내역 조회- (포인트 버튼 있는 곳에 있긴 함.)</span></p></body></html>"))
        self.point_lbl.setText(_translate("dialog", "포인트 페이지 입니다."))
        item = self.point_table.horizontalHeaderItem(0)
        item.setText(_translate("dialog", "회원번호"))
        item = self.point_table.horizontalHeaderItem(1)
        item.setText(_translate("dialog", "아이디"))
        item = self.point_table.horizontalHeaderItem(2)
        item.setText(_translate("dialog", "적립내역"))
        item = self.point_table.horizontalHeaderItem(3)
        item.setText(_translate("dialog", "사용내역"))
        self.point_btn_charity.setText(_translate("dialog", "기부하기"))
        self.point_btn__use.setText(_translate("dialog", "사용하기"))
        self.point_txt.setHtml(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- 나무를 심어 온실가스 절감이 가능하다는 문구 예전에 얘기했던 거 일단 넣었습니다</p></body></html>"))
        self.btn_my.setText(_translate("dialog", "MyPage"))
        self.btn_main.setText(_translate("dialog", "MainPage"))
        self.btn_result.setText(_translate("dialog", "결과"))
        self.btn_point.setText(_translate("dialog", "포인트"))
        self.btn_app.setText(_translate("dialog", "제품등록"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())

