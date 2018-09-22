from main.properties.prop import dbProp
import MySQLdb as conn
class dbConnect(object):

    def dbConnect(self):
        #pr=dbProp(section="",file="").dbProp()
        try:
            #-----------------connecting to db----------------#
            #dbconnection=conn.connect(pr.dbProp()+pr.dbProp("db.pass"))
            db = conn.connect(host="localhost",
                                 user="root",

                                 db="adesroot")
            print("Succesfully connected to: ",db)
            cs=db.cursor()
            sqlquery="select * from user_login"
            cs.execute(sqlquery)
            numrows = cs.rowcount
#_----------------selecting rows_____________#
            for x in range(0, numrows):
                row = cs.fetchone()
                print row[0], "-->", row[1]
                print row[2],"-->",row[4]
                #cs.commit()
                print("One row updated!")

                #--------------executing query---------------#
        except conn.Error as e:
            print("Error occurred: ",e)
db=dbConnect()
db.dbConnect()
        
