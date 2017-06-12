import pymysql


def get_mysql_db(user, passwd, database, domain="localhost"):
    return pymysql.connect(domain, user, passwd, database)


def insert_values(table_name, columns, values):
    sql = '''
        INSERT INTO %s(%s)VALUES(%s)
    ''' % (table_name, columns, values)
    return sql


def update_values(table_name, columns, new_values):
    return '''
        update %s set %s=%s
    '''.format(table_name, columns, new_values)
