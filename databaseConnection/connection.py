import  MySQLdb as mysql
class connt(object):
    def connct(self,username,password):
        self.username=username
        self.password=password

    def success(self):
        bool conn=False
        try:
            conn=mysql.connect(host="localhost",port="3306",user="root",pass="")

        except mysql.Error as e:
            print(e)

    def checkUsername(self):
        connt()
        connt.username="username"
        connt.password="password"
        if connt.username.:
            print("Successfully connected with user: ",connt.username)



