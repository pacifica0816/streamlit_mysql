import streamlit as st

from mysql_connection import get_connection

from mysql.connector.errors import Error

def run_select_app():
    st.subheader('데이터 조회')

    
    try :
        connection = get_connection()


        # 1. 전체 데이터 조회

        query = ''' select id, email, age, address 
                    from test_user; '''
        
        cursor = connection.cursor()

        cursor.execute(query)

        # select 문은 아래 내용이 필요하다.
        record_list = cursor.fetchall()
        print(record_list)

        for row in record_list :
            st.write(row)

        # 2. 아이디를 입력하면, 해당 아이디의 데이터만 조회
        st.subheader('아이디로 조회')
        id = st.number_input('아이디를 입력하세요',min_value=1)

        query = ''' select id, email, age, address
                    from test_user
                    where id = %s '''
        record = (id, )
        
        cursor.execute(query, record)

        # select 문은 아래 내용이 필요하다.
        record_list = cursor.fetchall()
        print(record_list)

        for row in record_list :
            st.write(row)

        # 3. 이메일 항목에서 검색하는 기능
        st.subheader('이메일 검색')
        search_word = st.text_input('검색어 입력')
        if st.button('검색하기!') :
            query = ''' select id, email, age, address
                        from test_user
                        where email like '%''' + search_word +'''%'; '''

            cursor.execute(query)

            # select 문은 아래 내용이 필요하다.
            record_list = cursor.fetchall()
            print(record_list)

            for row in record_list :
                st.write(row)


    # 위의 코드를 실행하다가, 문제가 생기면, except를 실행하라는 뜻.
    except Error as e :
        print('Error while connecting to MySQL', e)
    # finally 는 try에서 에러가 나든 안나든, 무조건 실행하라는 뜻.
    finally :
        print('finally')
        cursor.close()
        if connection.is_connected():
            connection.close()
            print('MySQL connection is closed')
        else :
            print('connection does not exist')