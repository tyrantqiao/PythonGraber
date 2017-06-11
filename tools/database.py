import pymysql


def get_mysql_db(user, passwd, database, domain="localhost"):
    return pymysql.connect(domain, user, passwd, database)


def insert_values(table_name, columns, values):
    return '''
        INSERT INTO %s(%s)VALUES (%s)
    '''.format(table_name,columns,values)
