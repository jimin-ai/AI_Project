# 필요한 함수들을 불러오기
import  sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
from DBcon import DBconn

# DBconn 파일과 연동
dbConn = DBconn()

#stacked만든 거 가져오기
from main import Ui_dialog
# from main_2 import btnTop_class

# BtnTop=btnTop_class()

#stacked한 것을 py파일로 변형하기(command에서함.지워도됨)
#pyuic5 -x project_hyun/project2/main.ui -o main.py



# 로그인 페이지 지정
login_class = uic.loadUiType("login.ui")[0]
# 회원가입 페이지 지정
join_class = uic.loadUiType("join.ui")[0]
# 회원가입 완료 페이지
joincheck_class = uic.loadUiType("joincheck.ui")[0]
# 로그인 실패
loginfail_class = uic.loadUiType("loginfail.ui")[0]
#-----------------------------------------------------!
#기부 성공페이지
charity_check_class = uic.loadUiType("charitycheck.ui")[0]

#-----------------------------------------------------!
#회원정보수정 페이지
member_update_class = uic.loadUiType("update.ui")[0]
# member_updatecheck_class = uic.loadUiType("project3/updatecheck.ui")
# 회원탈퇴 페이지
member_delete_class = uic.loadUiType("memberdelete.ui")[0]
# 회원탈퇴 입력 페이지
member_dlt_suc_class = uic.loadUiType("memberdeletesuccess.ui")[0]

#-----------------------------------------------------!
#기부성공페이지
class Charity_Check_Class(QDialog,charity_check_class):
    # 기본값 입력
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_charitycheck.clicked.connect(self.btn_charitycheck_close)

    def btn_charitycheck_close(self):
        Check.close()
#-----------------------------------------------------!        

# 로그인 페이지 클래스 지정
class Login_class(QDialog,login_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_con_join.clicked.connect(self.join_show)
        self.btn_con_login.clicked.connect(self.main_show)

    def join_show(self):
        Join.show()
        Login.close()
    def main_show(self):
        inputId = self.txt_login_id.text()
        inputPw = self.txt_login_pw.text()
        name = dbConn.login_select(inputId,inputPw)
        if name == 0:
            LoginFail.show()
        else:
            BtnTop.show()
            Login.close()


#로그인 실패 클래스
class LoginFail_class(QDialog,loginfail_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# 회원가입 페이지 클래스 지정
# 회원가입 완료 후 스타트페이지 열기
class Join_class(QDialog,join_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_join_commit.clicked.connect(self.joincheck_show)
    


    def joincheck_show(self):


        inputId=self.txt_id.text()
        inputPw=self.txt_pw.text()
        inputName=self.txt_name.text()
        inputPn=self.txt_phone.text()
        inputNum=self.txt_fam.text()
        result=dbConn.join_insert(inputId,inputPw,inputName,inputPn,int(inputNum))
        if result==0:
            print("회원가입 실패")
        else:
            print("회원가입 성공")
            self.txt_id.setText("")    #값초기화
            self.txt_pw.setText("")
            self.txt_name.setText("")
            self.txt_phone.setText("")
            self.txt_fam.setText("")
            JoinCheck.show()



# 회원가입 완료 페이지 클래스
class Joincheck_class(QDialog,joincheck_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_back_start.clicked.connect(self.login_show)
    
    def login_show(self):
        JoinCheck.close()
        Join.close()
        Login.show()


# 회원수정 페이지 클래스
class Member_Update_class(QDialog, member_update_class):
    # 기본값 입력
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.my_btn_updatedone.clicked.connect(self.member_update_close)

    def member_update_close(self):
        Update.close()
        # UpdateCheck.show()
        inputId = self.my_update_edit_id.text()
        inputPw = self.my_update_edit_pw.text()
        inputName = self.my_update_edit_name.text()
        inputPhone = self.my_update_edit_phone.text()
        inputFamily = self.my_update_edit_family.text()

        result = dbConn.update_all(inputId, inputPw, inputName, inputPhone, inputFamily)
        if result ==0:
            print("회원정보 수정 실패")
        else:
            print(inputId, '회원정보 수정 완료 !')
            self.my_update_edit_id.setText("")    #값초기화
            self.my_update_edit_pw.setText("")
            self.my_update_edit_name.setText("")
            self.my_update_edit_phone.setText("")
            self.my_update_edit_family.setText("")
        
    

# class Member_Updatecheck_class(QDialog, member_updatecheck_class):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)



# 회원탈퇴 선택 페이지 클래스
class Member_delete_class(QDialog,member_delete_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 회원탈퇴 선택 페이지에서 아니오 버튼설정
        self.btn_member_nodlt.clicked.connect(self.member_no_dlt_show)
        # 회원탈퇴 선택 페이지에서 예 버튼 설정
        self.btn_member_yesdlt.clicked.connect(self.member_yes_dlt_show)

    # 회원 탈퇴 아니오 누를시 회원탈퇴 선택 창 닫기
    def member_no_dlt_show(self):
        Memberdelete.close()

    # 회원탈퇴 선택 창 예 누를시 회원탈퇴 입력 창 열기
    # 회원탈퇴 선택 창 닫기
    def member_yes_dlt_show(self):
        Memberdltsuc.show()
        Memberdelete.close()

# 회원탈퇴 입력 창 클래스 지정하기
class Member_dlt_suc_class(QDialog,member_dlt_suc_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 회원탈퇴 입력 창에서 회원탈퇴 버튼 누르기 설정
        self.btn_member_dlt_push.clicked.connect(self.member_clear_show)

    # 버튼을 누르기 함수 설정
    def member_clear_show(self):
        # 아이디 입력값 받기
        inputId = self.member_dlt_id.text()
        # 비밀번호 입력값 받기
        inputPw = self.member_dlt_pw.text()
        # 입력값을 받아 DB에 보내 값이 맞는지 확인
        result = dbConn.join_delete(inputId,inputPw)
        # 반환 값이 0이면 아이디 아래 라벨에 다시 입력해주세요 출력
        if result == 0:
            self.lbl_delete_back.setText("다시 입력해주세요")
        # 반환값이 재대로 들어오면 회원탈퇴 입력 창 닫기
        else:
            Memberdltsuc.close()


# # 모델 검색 창 클래스
# class Model_search_class(QDialog,model_search_class):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         # 디비에 로그 값을 가져온다
#         result = dbConn.log()
#         # 디비에 로그1 값을 가져온다
#         result1 = dbConn.log1()
#         # 불러올 테이블 모델의 크기를 정한다 
#         self.app_model_search.setRowCount(30)
#         # 위 동일
#         self.app_model_search.setColumnCount(5)
#         # 리스트로 불러온 값을 다시 하나씩 입력하기 위해 for문 사용
#         for i in range(len(result1)):
#             # 값을 쉽게 입력하기 위해 변수 지정
#             a = result1[i]
#             # 모델에 i행 0열 에 a값 str로 입력
#             self.app_model_search.setItem(i,0, QTableWidgetItem(str(a)))
#         # 위와 동일 방법
#         for i in range(len(result)):
#             a = result[i]
#             self.app_model_search.setItem(i,1, QTableWidgetItem(str(a)))

#메인_2 페이지 클래스
class btnTop_class(QMainWindow, Ui_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_main.clicked.connect(self.set_funcFrame)
        self.btn_app.clicked.connect(self.set_funcFrame)
        self.btn_result.clicked.connect(self.set_funcFrame)
        self.btn_my.clicked.connect(self.set_funcFrame)
        self.btn_point.clicked.connect(self.set_funcFrame)
        #-----------------------------------------------------!
        #기부버튼 누르기
        self.point_btn_charity.clicked.connect(self.charity_class)
        #-----------------------------------------------------!
        self.stackedWidget.setCurrentIndex(0) #main페이지가 로그인 했을 때 첫번째로 뜨게함.
        # self.show()
        
        #회원정보 수정
        self.my_btn_update.clicked.connect(self.member_update_show)
        # 회원탈퇴페이지 쇼 버튼
        self.my_btn_delete.clicked.connect(self.memberdelete_show)
        # a=self.app_combo_type.currentText()
        self.app_btn_search.clicked.connect(self.app_search_show)
        # print(a)
    def app_search_show(self):
        combo_type_num = self.app_combo_type.currentIndex()

        # 청소기
        if combo_type_num == 0:
            Vc_name = dbConn.vc_name()
            # 디비에 값을 가져온다
            Vc_power = dbConn.vc_power()
            Vc_size = dbConn.vc_size()
            Vc_rating = dbConn.vc_rating()
            Vc_carbon = dbConn.vc_product()
            # 불러올 컬럼 수 정하기
            self.app_model_search.setColumnCount(5)
            # 리스트로 불러온 값을 다시 하나씩 입력하기 위해 for문 사용
            for i in range(len(Vc_name)):
                # 값을 쉽게 입력하기 위해 변수 지정
                a = Vc_name[i]
                # 불러올 값의 길이를(갯수) 정한다
                self.app_model_search.setRowCount(len(Vc_name))
                # 모델에 i행 0열 에 a값 str로 입력
                self.app_model_search.setItem(i,0, QTableWidgetItem(str(a))) 
            # 위와 동일 방법
            for i in range(len(Vc_power)):
                a = Vc_power[i]
                self.app_model_search.setRowCount(len(Vc_power))
                self.app_model_search.setItem(i,1, QTableWidgetItem(str(a)))
            for i in range(len(Vc_size)):
                a = Vc_size[i]
                self.app_model_search.setRowCount(len(Vc_size))
                self.app_model_search.setItem(i,2, QTableWidgetItem(str(a)))
            for i in range(len(Vc_rating)):
                a = Vc_rating[i]
                self.app_model_search.setRowCount(len(Vc_rating))
                self.app_model_search.setItem(i,3, QTableWidgetItem(str(a)))
            for i in range(len(Vc_carbon)):
                a = Vc_carbon[i]
                self.app_model_search.setRowCount(len(Vc_carbon))
                self.app_model_search.setItem(i,4, QTableWidgetItem(str(a)))

        # 전자렌지
        elif combo_type_num == 1:
            Mw_name = dbConn.mw_name()
            Mw_power = dbConn.mw_power()
            Mw_size = dbConn.mw_size()
            Mw_rating = dbConn.mw_rating()
            Mw_carbon = dbConn.mw_product()
            self.app_model_search.setColumnCount(5)
            for i in range(len(Mw_name)):
                a = Mw_name[i]
                self.app_model_search.setRowCount(len(Mw_name))
                self.app_model_search.setItem(i,0, QTableWidgetItem(str(a)))
            for i in range(len(Mw_power)):
                a = Mw_power[i]
                self.app_model_search.setRowCount(len(Mw_power))
                self.app_model_search.setItem(i,1, QTableWidgetItem(str(a)))
            for i in range(len(Mw_size)):
                a = Mw_size[i]
                self.app_model_search.setRowCount(len(Mw_size))
                self.app_model_search.setItem(i,2, QTableWidgetItem(str(a)))
            for i in range(len(Mw_rating)):
                a = Mw_rating[i]
                self.app_model_search.setRowCount(len(Mw_rating))
                self.app_model_search.setItem(i,3, QTableWidgetItem(str(a)))
            for i in range(len(Mw_carbon)):
                a = Mw_carbon[i]
                self.app_model_search.setRowCount(len(Mw_carbon))
                self.app_model_search.setItem(i,4, QTableWidgetItem(str(a)))

        #전기밥솥
        elif combo_type_num == 2:
            Rc_name = dbConn.rc_name()
            Rc_power = dbConn.rc_power()
            Rc_size = dbConn.rc_size()
            Rc_rating = dbConn.rc_rating()
            Rc_carbon = dbConn.rc_product()
            self.app_model_search.setColumnCount(5)
            for i in range(len(Rc_name)):
                a = Rc_name[i]
                self.app_model_search.setRowCount(len(Rc_name))
                self.app_model_search.setItem(i,0, QTableWidgetItem(str(a)))
            for i in range(len(Rc_power)):
                a = Rc_power[i]
                self.app_model_search.setRowCount(len(Rc_power))
                self.app_model_search.setItem(i,1, QTableWidgetItem(str(a)))
            for i in range(len(Rc_size)):
                a = Rc_size[i]
                self.app_model_search.setRowCount(len(Rc_size))
                self.app_model_search.setItem(i,2, QTableWidgetItem(str(a)))
            for i in range(len(Rc_rating)):
                a = Rc_rating[i]
                self.app_model_search.setRowCount(len(Rc_rating))
                self.app_model_search.setItem(i,3, QTableWidgetItem(str(a)))
            for i in range(len(Rc_carbon)):
                a = Rc_carbon[i]
                self.app_model_search.setRowCount(len(Rc_carbon))
                self.app_model_search.setItem(i,4, QTableWidgetItem(str(a)))

        # 에어컨
        elif combo_type_num == 3:
            Ac_name = dbConn.ac_name()
            Ac_power = dbConn.ac_power()
            Ac_size = dbConn.ac_size()
            Ac_rating = dbConn.ac_rating()
            Ac_carbon = dbConn.ac_product()
            self.app_model_search.setColumnCount(5)
            for i in range(len(Ac_name)):
                a = Ac_name[i]
                self.app_model_search.setRowCount(len(Ac_name))
                self.app_model_search.setItem(i,0, QTableWidgetItem(str(a)))
            for i in range(len(Ac_power)):
                a = Ac_power[i]
                self.app_model_search.setRowCount(len(Ac_power))
                self.app_model_search.setItem(i,1, QTableWidgetItem(str(a)))
            for i in range(len(Ac_size)):
                a = Ac_size[i]
                self.app_model_search.setRowCount(len(Ac_size))
                self.app_model_search.setItem(i,2, QTableWidgetItem(str(a)))
            for i in range(len(Ac_rating)):
                a = Ac_rating[i]
                self.app_model_search.setRowCount(len(Ac_rating))
                self.app_model_search.setItem(i,3, QTableWidgetItem(str(a)))
            for i in range(len(Ac_carbon)):
                a = Ac_carbon[i]
                self.app_model_search.setRowCount(len(Ac_carbon))
                self.app_model_search.setItem(i,4, QTableWidgetItem(str(a)))

        # 세탁기
        elif combo_type_num == 4:
            Ws_name = dbConn.ws_name()
            Ws_power = dbConn.ws_power()
            Ws_size = dbConn.ws_size()
            Ws_rating = dbConn.ws_rating()
            Ws_carbon = dbConn.ws_product()
            self.app_model_search.setColumnCount(5)
            for i in range(len(Ws_name)):
                a = Ws_name[i]
                self.app_model_search.setRowCount(len(Ws_name))
                self.app_model_search.setItem(i,0, QTableWidgetItem(str(a)))
            for i in range(len(Ws_power)):
                a = Ws_power[i]
                self.app_model_search.setRowCount(len(Ws_power))
                self.app_model_search.setItem(i,1, QTableWidgetItem(str(a)))
            for i in range(len(Ws_size)):
                a = Ws_size[i]
                self.app_model_search.setRowCount(len(Ws_size))
                self.app_model_search.setItem(i,2, QTableWidgetItem(str(a)))
            for i in range(len(Ws_rating)):
                a = Ws_rating[i]
                self.app_model_search.setRowCount(len(Ws_rating))
                self.app_model_search.setItem(i,3, QTableWidgetItem(str(a)))
            for i in range(len(Ws_carbon)):
                a = Ws_carbon[i]
                self.app_model_search.setRowCount(len(Ws_carbon))
                self.app_model_search.setItem(i,4, QTableWidgetItem(str(a)))

        # 티브이
        elif combo_type_num == 5:
            Tv_name = dbConn.tv_name()
            Tv_power = dbConn.tv_power()
            Tv_size = dbConn.tv_size()
            Tv_rating = dbConn.tv_rating()
            Tv_carbon = dbConn.tv_product()
            self.app_model_search.setColumnCount(5)
            for i in range(len(Tv_name)):
                a = Tv_name[i]
                self.app_model_search.setRowCount(len(Tv_name))
                self.app_model_search.setItem(i,0, QTableWidgetItem(str(a)))
            for i in range(len(Tv_power)):
                a = Tv_power[i]
                self.app_model_search.setRowCount(len(Tv_power))
                self.app_model_search.setItem(i,1, QTableWidgetItem(str(a)))
            for i in range(len(Tv_size)):
                a = Tv_size[i]
                self.app_model_search.setRowCount(len(Tv_size))
                self.app_model_search.setItem(i,2, QTableWidgetItem(str(a)))
            for i in range(len(Tv_rating)):
                a = Tv_rating[i]
                self.app_model_search.setRowCount(len(Tv_rating))
                self.app_model_search.setItem(i,3, QTableWidgetItem(str(a)))
            for i in range(len(Tv_carbon)):
                a = Tv_carbon[i]
                self.app_model_search.setRowCount(len(Tv_carbon))
                self.app_model_search.setItem(i,4, QTableWidgetItem(str(a)))

        # 냉장고
        elif combo_type_num == 6:
            Rf_name = dbConn.rf_name()
            Rf_power = dbConn.rf_power()
            Rf_size = dbConn.rf_size()
            Rf_rating = dbConn.rf_rating()
            Rf_carbon = dbConn.rf_product()
            self.app_model_search.setColumnCount(5)
            for i in range(len(Rf_name)):
                a = Rf_name[i]
                self.app_model_search.setRowCount(len(Rf_name))
                self.app_model_search.setItem(i,0, QTableWidgetItem(str(a)))
            for i in range(len(Rf_power)):
                a = Rf_power[i]
                self.app_model_search.setRowCount(len(Rf_power))
                self.app_model_search.setItem(i,1, QTableWidgetItem(str(a)))
            for i in range(len(Rf_size)):
                a = Rf_size[i]
                self.app_model_search.setRowCount(len(Rf_size))
                self.app_model_search.setItem(i,2, QTableWidgetItem(str(a)))
            for i in range(len(Rf_rating)):
                a = Rf_rating[i]
                self.app_model_search.setRowCount(len(Rf_rating))
                self.app_model_search.setItem(i,3, QTableWidgetItem(str(a)))
            for i in range(len(Rf_carbon)):
                a = Rf_carbon[i]
                self.app_model_search.setRowCount(len(Rf_carbon))
                self.app_model_search.setItem(i,4, QTableWidgetItem(str(a)))
 
     def app_search_show(self):
        combo_type_num = self.app_combo_type.currentIndex()

        # 청소기
        if combo_type_num == 0:
            Vc_name = dbConn.vc_name()
            # 디비에 값을 가져온다
            Vc_power = dbConn.vc_power()
            Vc_size = dbConn.vc_size()
            Vc_rating = dbConn.vc_rating()
            Vc_carbon = dbConn.vc_product()
            # 불러올 컬럼 수 정하기
            self.app_model_search.setColumnCount(5)
            # 리스트로 불러온 값을 다시 하나씩 입력하기 위해 for문 사용
            for i in range(len(Vc_name)):
                # 값을 쉽게 입력하기 위해 변수 지정
                a = Vc_name[i]
                # 불러올 값의 길이를(갯수) 정한다
                self.app_model_search.setRowCount(len(Vc_name))
                # 모델에 i행 0열 에 a값 str로 입력
                self.app_model_search.setItem(i,0, QTableWidgetItem(str(a))) 
            # 위와 동일 방법
            for i in range(len(Vc_power)):
                a = Vc_power[i]
                self.app_model_search.setRowCount(len(Vc_power))
                self.app_model_search.setItem(i,1, QTableWidgetItem(str(a)))
            for i in range(len(Vc_size)):
                a = Vc_size[i]
                self.app_model_search.setRowCount(len(Vc_size))
                self.app_model_search.setItem(i,2, QTableWidgetItem(str(a)))
            for i in range(len(Vc_rating)):
                a = Vc_rating[i]
                self.app_model_search.setRowCount(len(Vc_rating))
                self.app_model_search.setItem(i,3, QTableWidgetItem(str(a)))
            for i in range(len(Vc_carbon)):
                a = Vc_carbon[i]
                self.app_model_search.setRowCount(len(Vc_carbon))
                self.app_model_search.setItem(i,4, QTableWidgetItem(str(a)))

        # 전자렌지
        elif combo_type_num == 1:
            Mw_name = dbConn.mw_name()
            Mw_power = dbConn.mw_power()
            Mw_size = dbConn.mw_size()
            Mw_rating = dbConn.mw_rating()
            Mw_carbon = dbConn.mw_product()
            self.app_model_search.setColumnCount(5)
            for i in range(len(Mw_name)):
                a = Mw_name[i]
                self.app_model_search.setRowCount(len(Mw_name))
                self.app_model_search.setItem(i,0, QTableWidgetItem(str(a)))
            for i in range(len(Mw_power)):
                a = Mw_power[i]
                self.app_model_search.setRowCount(len(Mw_power))
                self.app_model_search.setItem(i,1, QTableWidgetItem(str(a)))
            for i in range(len(Mw_size)):
                a = Mw_size[i]
                self.app_model_search.setRowCount(len(Mw_size))
                self.app_model_search.setItem(i,2, QTableWidgetItem(str(a)))
            for i in range(len(Mw_rating)):
                a = Mw_rating[i]
                self.app_model_search.setRowCount(len(Mw_rating))
                self.app_model_search.setItem(i,3, QTableWidgetItem(str(a)))
            for i in range(len(Mw_carbon)):
                a = Mw_carbon[i]
                self.app_model_search.setRowCount(len(Mw_carbon))
                self.app_model_search.setItem(i,4, QTableWidgetItem(str(a)))

        #전기밥솥
        elif combo_type_num == 2:
            Rc_name = dbConn.rc_name()
            Rc_power = dbConn.rc_power()
            Rc_size = dbConn.rc_size()
            Rc_rating = dbConn.rc_rating()
            Rc_carbon = dbConn.rc_product()
            self.app_model_search.setColumnCount(5)
            for i in range(len(Rc_name)):
                a = Rc_name[i]
                self.app_model_search.setRowCount(len(Rc_name))
                self.app_model_search.setItem(i,0, QTableWidgetItem(str(a)))
            for i in range(len(Rc_power)):
                a = Rc_power[i]
                self.app_model_search.setRowCount(len(Rc_power))
                self.app_model_search.setItem(i,1, QTableWidgetItem(str(a)))
            for i in range(len(Rc_size)):
                a = Rc_size[i]
                self.app_model_search.setRowCount(len(Rc_size))
                self.app_model_search.setItem(i,2, QTableWidgetItem(str(a)))
            for i in range(len(Rc_rating)):
                a = Rc_rating[i]
                self.app_model_search.setRowCount(len(Rc_rating))
                self.app_model_search.setItem(i,3, QTableWidgetItem(str(a)))
            for i in range(len(Rc_carbon)):
                a = Rc_carbon[i]
                self.app_model_search.setRowCount(len(Rc_carbon))
                self.app_model_search.setItem(i,4, QTableWidgetItem(str(a)))

        # 에어컨
        elif combo_type_num == 3:
            Ac_name = dbConn.ac_name()
            Ac_power = dbConn.ac_power()
            Ac_size = dbConn.ac_size()
            Ac_rating = dbConn.ac_rating()
            Ac_carbon = dbConn.ac_product()
            self.app_model_search.setColumnCount(5)
            for i in range(len(Ac_name)):
                a = Ac_name[i]
                self.app_model_search.setRowCount(len(Ac_name))
                self.app_model_search.setItem(i,0, QTableWidgetItem(str(a)))
            for i in range(len(Ac_power)):
                a = Ac_power[i]
                self.app_model_search.setRowCount(len(Ac_power))
                self.app_model_search.setItem(i,1, QTableWidgetItem(str(a)))
            for i in range(len(Ac_size)):
                a = Ac_size[i]
                self.app_model_search.setRowCount(len(Ac_size))
                self.app_model_search.setItem(i,2, QTableWidgetItem(str(a)))
            for i in range(len(Ac_rating)):
                a = Ac_rating[i]
                self.app_model_search.setRowCount(len(Ac_rating))
                self.app_model_search.setItem(i,3, QTableWidgetItem(str(a)))
            for i in range(len(Ac_carbon)):
                a = Ac_carbon[i]
                self.app_model_search.setRowCount(len(Ac_carbon))
                self.app_model_search.setItem(i,4, QTableWidgetItem(str(a)))

        # 세탁기
        elif combo_type_num == 4:
            Ws_name = dbConn.ws_name()
            Ws_power = dbConn.ws_power()
            Ws_size = dbConn.ws_size()
            Ws_rating = dbConn.ws_rating()
            Ws_carbon = dbConn.ws_product()
            self.app_model_search.setColumnCount(5)
            for i in range(len(Ws_name)):
                a = Ws_name[i]
                self.app_model_search.setRowCount(len(Ws_name))
                self.app_model_search.setItem(i,0, QTableWidgetItem(str(a)))
            for i in range(len(Ws_power)):
                a = Ws_power[i]
                self.app_model_search.setRowCount(len(Ws_power))
                self.app_model_search.setItem(i,1, QTableWidgetItem(str(a)))
            for i in range(len(Ws_size)):
                a = Ws_size[i]
                self.app_model_search.setRowCount(len(Ws_size))
                self.app_model_search.setItem(i,2, QTableWidgetItem(str(a)))
            for i in range(len(Ws_rating)):
                a = Ws_rating[i]
                self.app_model_search.setRowCount(len(Ws_rating))
                self.app_model_search.setItem(i,3, QTableWidgetItem(str(a)))
            for i in range(len(Ws_carbon)):
                a = Ws_carbon[i]
                self.app_model_search.setRowCount(len(Ws_carbon))
                self.app_model_search.setItem(i,4, QTableWidgetItem(str(a)))

        # 티브이
        elif combo_type_num == 5:
            Tv_name = dbConn.tv_name()
            Tv_power = dbConn.tv_power()
            Tv_size = dbConn.tv_size()
            Tv_rating = dbConn.tv_rating()
            Tv_carbon = dbConn.tv_product()
            self.app_model_search.setColumnCount(5)
            for i in range(len(Tv_name)):
                a = Tv_name[i]
                self.app_model_search.setRowCount(len(Tv_name))
                self.app_model_search.setItem(i,0, QTableWidgetItem(str(a)))
            for i in range(len(Tv_power)):
                a = Tv_power[i]
                self.app_model_search.setRowCount(len(Tv_power))
                self.app_model_search.setItem(i,1, QTableWidgetItem(str(a)))
            for i in range(len(Tv_size)):
                a = Tv_size[i]
                self.app_model_search.setRowCount(len(Tv_size))
                self.app_model_search.setItem(i,2, QTableWidgetItem(str(a)))
            for i in range(len(Tv_rating)):
                a = Tv_rating[i]
                self.app_model_search.setRowCount(len(Tv_rating))
                self.app_model_search.setItem(i,3, QTableWidgetItem(str(a)))
            for i in range(len(Tv_carbon)):
                a = Tv_carbon[i]
                self.app_model_search.setRowCount(len(Tv_carbon))
                self.app_model_search.setItem(i,4, QTableWidgetItem(str(a)))

        # 냉장고
        elif combo_type_num == 6:
            Rf_name = dbConn.rf_name()
            Rf_power = dbConn.rf_power()
            Rf_size = dbConn.rf_size()
            Rf_rating = dbConn.rf_rating()
            Rf_carbon = dbConn.rf_product()
            self.app_model_search.setColumnCount(5)
            for i in range(len(Rf_name)):
                a = Rf_name[i]
                self.app_model_search.setRowCount(len(Rf_name))
                self.app_model_search.setItem(i,0, QTableWidgetItem(str(a)))
            for i in range(len(Rf_power)):
                a = Rf_power[i]
                self.app_model_search.setRowCount(len(Rf_power))
                self.app_model_search.setItem(i,1, QTableWidgetItem(str(a)))
            for i in range(len(Rf_size)):
                a = Rf_size[i]
                self.app_model_search.setRowCount(len(Rf_size))
                self.app_model_search.setItem(i,2, QTableWidgetItem(str(a)))
            for i in range(len(Rf_rating)):
                a = Rf_rating[i]
                self.app_model_search.setRowCount(len(Rf_rating))
                self.app_model_search.setItem(i,3, QTableWidgetItem(str(a)))
            for i in range(len(Rf_carbon)):
                a = Rf_carbon[i]
                self.app_model_search.setRowCount(len(Rf_carbon))
                self.app_model_search.setItem(i,4, QTableWidgetItem(str(a)))   

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
            elif btn_c.objectName() == "btn_result":
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

    #-----------------------------------------------------!
    def charity_class(self):
        Check.show()
    #-----------------------------------------------------!
    #회원 정보 수정
    def member_update_show(self):
        Update.show()
    
    # 회원탈퇴 페이지 쇼
    def memberdelete_show(self):
        Memberdelete.show()

    





if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 로그인 페이지 클래스 변수 지정
    Login = Login_class()
    Login.show()
    #로그인 페이지 실패 클래스 변수 지정
    LoginFail = LoginFail_class()
    # 회원가입 페이지 클래스 변수 지정
    Join = Join_class()
    # 회원가입 완료 페이지 클래스 변수 지정
    JoinCheck = Joincheck_class()
    #stacked된 페이지 클래스 변수 지정
    BtnTop = btnTop_class()
    #-----------------------------------------------------!
    #기부성공
    Check = Charity_Check_Class()
    #-----------------------------------------------------!

    #회원정보 수정
    Update = Member_Update_class()
    # UpdateCheck = Member_Updatecheck_class()
    # 회원탈퇴
    Memberdelete = Member_delete_class()
    Memberdltsuc = Member_dlt_suc_class()





    app.exec_()
