import streamlit as st
from mysql_connection import get_connection
from mysql.connector.errors import Error

def run_delete_app():
    st.subheader('유저 삭제')

    id = st.number_input('삭제할 아이디 입력', min_value=1)

    if st.button('삭제!'):
        try :
            # 1. DB 에 연결
            connection = get_connection()
            
            # 2. 쿼리문 만들고
            query = '''delete from test_user
                        where id = %s;'''
            # 파이썬에서, 튜플만들때, 데이터가 1개인 경우에는 콤마를 꼭
            # 써준다.
            record = (id,)
            
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

                st.write('삭제가 완료 되었습니다.')