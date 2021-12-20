import streamlit as st

import mysql.connector
from mysql_connection import get_connection

def run_insert_app():
    st.subheader('회원가입')

    email = st.text_input('이메일 입력')
    password = st.text_input('비밀번호입력', type='password', max_chars=12)
    age = st.number_input('나이 입력', min_value=1)
    address = st.text_input('주소 입력')

    if st.button('저장하기') :
        try :
            # 1. DB 에 연결
            connection = get_connection()

            # 2. 쿼리문 만들고
            query = '''insert into test_user
                        (email, password, age, address)
                        values
                        (%s, %s, %s, %s);'''
            # 파이썬에서, 튜플만들때, 데이터가 1개인 경우에는 콤마를 꼭
            # 써준다.
            record = (email,password,age,address)
            
            # 3. 커넥션으로부터 커서를 가져온다.
            cursor = connection.cursor()

            # 4. 쿼리문을 커서에 넣어서 실행한다.
            cursor.execute(query, record)

            # 5. 커넥션을 커밋한다.=> 디비에 영구적으로 반영하라는 뜻.
            connection.commit()

        except mysql.connector.Error as e:
            print('Error ', e)
        finally :
            if connection.is_connected():
                cursor.close()
                connection.close()
                print('MySQL connection is closed')
                st.write('회원 정보가 잘 저장되었습니다.')