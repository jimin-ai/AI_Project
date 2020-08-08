import pymysql as ps
import pandas as pd


class DBconn:
    def __init__(self):
        self.db = ps.connect(
            host='172.30.1.20',
            port=3306,
            user='project',
            passwd='123456',
            db='project',
            charset='utf8')
        
        self.cursor = self.db.cursor(ps.cursors.DictCursor)


    def join_insert(self,inputId,inputPw,inputName,inputPn,inputFam):
        sql=f"""insert into member(MEMBER_ID,MEMBER_PW,MEMBER_NAME,MEMBER_PHONE,FAMILY) 
        values('{inputId}','{inputPw}','{inputName}','{inputPn}',{inputFam})"""
        result = self.cursor.execute(sql)
        self.db.commit()
        return result

    def login_select(self,inputId,inputPw):
        sql=f"select MEMBER_NAME from member where MEMBER_ID='{inputId}' and MEMBER_PW = '{inputPw}'"
        result = self.cursor.execute(sql)
        name = self.cursor.fetchall()
        if result == 0:
            return 0
        else:
            return name

    def join_delete(self,input_id,pw):
        sql = f"delete from member where MEMBER_ID='{input_id}' AND MEMBER_PW='{pw}'"
        result = self.cursor.execute(sql)
        self.db.commit()
        return result

    # 셀렉트 할 함수를 정의한다
    def log1(self):
        # 셀렉트 값이 딕셔너리라 리스트 값으로 변경하기 위해
        # 빈 리스트 값을 지정해준다
        ho_list=[]
        # 값을 불러온다
        select_sql = "select * from homeappliances"
        # 값을 불러온다
        self.cursor.execute(select_sql)
        # 불러온 값을 저장한다
        result=self.cursor.fetchall()
        # 불러올 값을 for문으로 하나씩 리스트값에 append 해준다
        # 컬럼 형식의 열 값을 출력하기에 컬럼 명을 써준다
        for i in result:
            ho_list.append(i['MODEL_NAME'])
        # 값을 반환해준다
        return ho_list

    # 위와 동일
    def log(self):
        ho_list=[]
        select_sql = "select * from homeappliances"
        self.cursor.execute(select_sql)
        result=self.cursor.fetchall()
        for i in result:
            ho_list.append(i['POWER'])
        return ho_list

    # def log(self):
    #     pri_list=[]
    #     select_sql = "select * from member"
    #     self.cursor.execute(select_sql)
    #     dic_list=self.cursor.fetchall()
    #     for dic_change in dic_list:
    #         pri_list.append(dic_change['MEMBER_ID'])
    #     # df=pd.DataFrame(result)
    #     return pri_list