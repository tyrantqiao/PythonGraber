import pymysql

from tools.database import get_mysql_db, insert_values

db = pymysql.connect("localhost", "root", "1YTINTERNshipQsql", "posts")
cursor = db.cursor()
# cursor.execute("Drop TABLE if EXISTS POPULAR")

popular_table_sql = """
    CREATE TABLE POPULAR(
        POST_TITLE CHAR(50) NOT NULL, 
        POST_URL CHAR(100) NOT NULL ,
        COMHEAD CHAR(20) NOT NULL ,
        SAVE_PATH CHAR(50) DEFAULT NULL,
        DOWNLOAD_FLAG CHAR(0) DEFAULT NULL
        ) 
"""

post_table_sql = '''
    CREATE TABLE POST(
      TITLE CHAR(50) NOT NULL ,
      AUTHOR CHAR(20) DEFAULT NULL,
      TXT_PATH CHAR(50) NOT NULL,
      RESOURCES_PATH CHAR(50) DEFAULT NULL
    )
'''

insert_sql = insert_values('popular',
                           'POST_TITLE,POST_URL,COMHEAD',
                           '''
                            '初窥dep', 'http://tonybai.com/2017/06/08/first-glimpse-of-dep/', 'tonybai.com'
                        ''')
print(insert_sql)
cursor.execute(insert_sql)
db.close()
