import streamlit as st
from mysql_connection import get_connection
from mysql.connector.errors import Error

def run_update_app() :
    st.subheader('아이디로, 나이를 업데이트')

    id = st.number_input('아이디 입력', min_value=1)
    age = st.number_input('나이 입력', min_value=1)

    if st.button('저장') :
        try :
            # 1. DB 에 연결
            connection = get_connection()

            # 2. 쿼리문 만들고
            query = '''update test_user
                        set age = %s 
                        where id = %s;'''
            # 파이썬에서, 튜플만들때, 데이터가 1개인 경우에는 콤마를 꼭
            # 써준다.
            record = (age, id)
            
            # 3. 커넥션으로부터 커서를 가져온다.
            cursor = connection.cursor()

            # 4. 쿼리문을 커서에 넣어서 실행한다.
            cursor.execute(query, record)

            # 5. 커넥션을 커밋한다.=> 디비에 영구적으로 반영하라는 뜻.
            connection.commit()

        except Error as e:
            print('Error ', e)
        finally :
            if connection.is_connected():
                cursor.close()
                connection.close()
                print('MySQL connection is closed')

                st.write('변경이 완료 되었습니다.')