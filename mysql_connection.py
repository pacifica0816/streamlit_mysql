import mysql.connector
from mysql_connection import get_connection

def get_connection() :
    connection = mysql.connector.connect(
        host = 'yh-db.ce8mtmot71ct.ap-northeast-2.rds.amazonaws.com',
        database = 'streamlit_db',
        user = 'admin',
        password = 'kk007625'
    )
    return connection
    