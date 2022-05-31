import mysql.connector


class DB:
    host = None
    database = None
    user = None
    password = None
    connection = None
    cursor = None

    def __init__(self):
        self.startDB()

    def startDB(self):
        self.host = 'localhost'
        self.database = "sulDump"
        self.user = 'root'
        self.password = 'THimberland0&1'

        try:
            self.connection = mysql.connector.connect(host=self.host,
                                                      database=self.database,
                                                      user=self.user,
                                                      password=self.password)
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                self.cursor = self.connection.cursor()
                print(f"You are connected to {self.database}")
        except mysql.connector.errors.IntegrityError as e:
            print(e)

    def insertTitle(self, data):
        query = f"insert into title(sulID,title,category,subCategory) VALUES(%s,%s,%s,%s)"
        val = data
        self.cursor.execute(query, val)
        self.connection.commit()

    def insertVerse(self, data):
        query = f"insert into verses(sulID,verseNo,verse) VALUES(%s,%s,%s)"
        val = data
        self.cursor.execute(query, val)
        self.connection.commit()

    def insertChorus(self, data):
        query = f"insert into chorus(sulID,chorus) VALUES(%s,%s)"
        val = data
        self.cursor.execute(query, val)
        self.connection.commit()

    def getVerses(self, sul):
        self.cursor.execute(f"select * from verses Where(sulID = '{sul}')")
        a = self.cursor.fetchall()
        return a

    def getChorus(self, sul):
        self.cursor.execute(f"select * from chorus Where(sulID = '{sul}')")
        a = self.cursor.fetchall()
        return a

    def getTitle(self, sul):
        self.cursor.execute(f"select * from title Where(sulID = '{sul}')")
        a = self.cursor.fetchall()
        return a
    def getAllTitles(self):
        self.cursor.execute(f"select * from title")
        a = self.cursor.fetchall()
        return a
