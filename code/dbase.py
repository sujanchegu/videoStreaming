import sqlite3
from sqlite3 import Error

class DBase:
    def __init__(self):
        self.__conn = None
        try:
            self.__conn = sqlite3.connect('../assets/database.db')
            
            self.__conn.execute('DROP TABLE IF EXISTS videos')
            self.__conn.execute('''CREATE TABLE videos (name TEXT, uri TEXT,
            desc TEXT, likes INTEGER, views INTEGER, email TEXT, dur REAL)''')

            self.__conn.execute('DROP TABLE IF EXISTS users')
            self.__conn.execute('''CREATE TABLE users (name TEXT, email TEXT CONSTRAINT email_is_pkey PRIMARY KEY,
            passwd TEXT, regDate TEXT, creditCard TEXT, isCreator INTEGER)''')
        except Error as e:
            print("__init__", e)

    def addVideoToDB(self, iName, iURI, iDesc, iEmail, iDur, iLikes=0, iViews=0):
        try:
            params = (iName, iURI, iDesc, iLikes, iViews, iEmail, iDur)
            self.__conn.execute('INSERT INTO videos VALUES (?, ?, ?, ?, ?, ?, ?)', params)
        except Error as e:
            print(e)

    def deleteVideoFromDB(self, iURI):
        try:
            self.__conn.execute(f'DELETE FROM videos WHERE uri = "{iURI}"')
        except Error as e:
            print("deleteVideoFromDB", e)

    def calcSimilarity(self, iURI1, iURI2):
        pass
    
    def incAttr(self, iURI, iAttr, iCount=1):
        try:
            self.__conn.execute(f'UPDATE videos SET {iAttr} = {iAttr} \
            + {iCount} WHERE uri = "{iURI}"')
        except Error as e:
            print("incAttr", e)

    def regUser(self, iName, iEmail, iPassword, iRegDate, iCCard=None, iIsCreator=0):
        try:
            params = (iName, iEmail, iPassword, iRegDate, iCCard, iIsCreator)
            self.__conn.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)', params)
        except Error as e:
            print("regUser", e)

    def regCreator(self, iEmail):
        try:
            self.__conn.execute(f'UPDATE users SET isCreator = 1 WHERE email = "{iEmail}"')
        except Error as e:
            print("regCreator", e)

    def checkUser(self, iEmail):
        try:
            csor = self.__conn.cursor()
            csor.execute(f'SELECT EXISTS (SELECT 1 FROM users WHERE email ="{iEmail}")')
            if(csor.fetchall()[0][0] == 0):
                return False
            else:
                return True
        except Error as e:
            print("checkUser", e)

    #DEBUG SHIT
    def sampleaddvideo(self):
        self.__conn.execute("INSERT INTO videos VALUES (?, ?, ?, ?, ?, ?, ?)", ('sriram eating', '6248fads', 'bennur too', 123, 456, '9fbc67', 23.45))

    #DEBUG SHIT
    def print_table(self):
        cur = self.__conn.cursor()
        cur.execute('SELECT * from users')
        print(cur.fetchall())
        cur.execute('SELECT * from videos')
        print(cur.fetchall())


db = DBase()
db.regUser('abc', 'abcgmail.com', 'passwd', '12-12-2012', '456456456456', 0)
print(db.checkUser('9fbc67'))
db.regCreator('abcgmail.com')
print(db.checkUser('abcgmail.com'))
db.sampleaddvideo()
db.incAttr('6248fads', 'views', 5)
db.print_table()