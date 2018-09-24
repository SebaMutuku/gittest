from Web.Database import dbConnection
from MySQLdb import MySQLError,connections
import MySQLdb as mysql
class Login(object):
    def login(self):
        db=dbConnection()
        sql="select username from user_login where username=?"
        try:
            conn=db
            try:
                cur=conn.cursor
                cur.execute(sql)
            except connections.Error as er:
                print (er)
        except MySQLError as e:
            print (e)

Lg=Login().login()
print (Lg)
