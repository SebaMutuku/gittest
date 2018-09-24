import MySQLdb.connections
import MySQLdb as mysql

class database(object):
    def __init__(self,dbUser,dbPass):
        self.dbUser=dbUser
        self.dbPass=dbPass
    @staticmethod
    def dbConnect():
        dbUser='root'
        dbPass='root'
        host='localhost'
        port='3306'
        dbName='adesroot'
        try:
            conn=mysql.connect(host,dbUser,dbPass,dbName)
            print ("Successfully connected to database",conn)
            return conn
        except (MySQLdb.Error,MySQLdb.Warning) as e:
            print(e)
            print ("Not connected to database")



db=database(dbUser="root",dbPass="").dbConnect()
print(db)



