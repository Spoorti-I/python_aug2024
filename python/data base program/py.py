import sys
import pymysql

class DbOperationException(Exception):
    pass

class bill:
    def connectDb(self):
        conn = pymysql.Connect(
            host='localhost', port=3306,
            user='root', password='Root123',
            db='spoorti_db', charset='utf8')
        print('Database connected successfully')
        return conn

    def disConnectDb(self, connection):
        connection.close()
        print('Database disconnected')
