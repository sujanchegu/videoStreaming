import sqlite3
from sqlite3 import Error
import os
from bs4 import BeautifulSoup

class DBase:
    def __init__(self):
        self.__conn = None
        try:
            self.__conn = sqlite3.connect('../assets/database.db', check_same_thread=False)
            
            self.__conn.execute('DROP TABLE IF EXISTS videos')
            self.__conn.execute('''CREATE TABLE videos (name TEXT, uri TEXT,
            desc TEXT, likes INTEGER, views INTEGER, email TEXT, dur REAL)''')

            self.__conn.execute('DROP TABLE IF EXISTS users')
            self.__conn.execute('''CREATE TABLE users (name TEXT, email TEXT CONSTRAINT email_is_pkey PRIMARY KEY,
            passwd TEXT, regDate TEXT, creditCard TEXT, isCreator INTEGER)''')
        except Error as e:
            print("dbase::__init__", e)

    def addVideoToDB(self, iName, iURI, iDesc, iEmail, iDur, iLikes=0, iViews=0):
        try:
            params = (iName, iURI, iDesc, iLikes, iViews, iEmail, iDur)
            self.__conn.execute('INSERT INTO videos VALUES (?, ?, ?, ?, ?, ?, ?)', params)
            self.__conn.commit()
        except Error as e:
            print("dbase::addVideoToDB", e)

    def deleteVideoFromDB(self, iURI):
        try:
            self.__conn.execute(f'DELETE FROM videos WHERE uri = "{iURI}"')
            os.remove("../assets/videos/" + iURI + '.mp4')
            self.__conn.commit()
        except Error as e:
            print("dbase::deleteVideoFromDB", e)

    def FindSimilar(self, iURI1):
        return iURI
    
    def incAttr(self, iURI, iAttr, iCount=1):
        try:
            self.__conn.execute(f'UPDATE videos SET {iAttr} = {iAttr} + {iCount} WHERE uri = "{iURI}"')
            self.__conn.commit()
        except Error as e:
            print("dbase::incAttr", e)

    def regUser(self, iName, iEmail, iPassword, iRegDate, iCCard=None, iIsCreator=0):
        try:
            params = (iName, iEmail, iPassword, iRegDate, iCCard, iIsCreator)
            self.__conn.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)', params)
            self.__conn.execute(f'CREATE TABLE [{iEmail}] (uri TEXT, count INTEGER, session INTEGER)')
            self.__conn.commit()
        except Error as e:
            print("dbase::regUser", e)

    def regCreator(self, iEmail):
        try:
            self.__conn.execute(f'UPDATE users SET isCreator = 1 WHERE email = "{iEmail}"')
            self.__conn.commit()
        except Error as e:
            print("dbase::regCreator", e)

    def checkUser(self, iEmail):
        try:
            csor = self.__conn.cursor()
            csor.execute(f'SELECT EXISTS (SELECT 1 FROM users WHERE email ="{iEmail}")')
            if(csor.fetchall()[0][0] == 0):
                return False
            else:
                return True
        except Error as e:
            print("dbase::checkUser", e)

    def retriveUser(self, iEmail):
        try:
            csor = self.__conn.cursor()
            csor.execute(f'SELECT * FROM users WHERE email = {iEmail}')
            return csor.fetchall()
        except Error as e:
            print("dbase::retriveUser", e)
    
    def addHistoryToDB(self, iHistoryObject):
        try:
            iEmail = iHistoryObject.__uid
            csor = self.__conn.cursor()
            csor.execute(f'SELECT MAX(session) FROM [{iEmail}]')
            print(csor.fetchall())
            for iVideoObject,iCount in iHistoryObject.items():
                iURI = iVideoObject.__name
                csor.execute(f'SELECT EXISTS (SELECT 1 FROM users WHERE uri ="{iURI}")')
                if(csor.fetchall()[0][0] == 0):
                    csor.execute(f'INSERT INTO [{iEmail}] values (?, ?, ?)', (iURI, icount, iSessionNo))
                    csor.commit()
                else:
                    csor.execute(f'UPDATE [{iEmail}] SET session = session + {iCount} WHERE uri = {iURI}')
                    csor.commit()
            self.__conn.commit()
        except Error as e:
            print("dbase::addHistoryToDB", e)

    #DEBUG SHIT
    def print_table(self):
        cur = self.__conn.cursor()
        cur.execute('SELECT * from users')
        print(cur.fetchall())
        cur.execute('SELECT * from videos')
        print(cur.fetchall())



db = DBase()
db.regUser('abc', 'abc@gmail.com', 'passwd', '12-12-2012', '456456456456', 0)
print(db.checkUser('9fbc67'))
db.regCreator('abc@gmail.com')
print(db.checkUser('abc@gmail.com'))
os.system('touch ../assets/videos/6248fads.mp4')
db.addVideoToDB('sriram eating', '6248fads', 'bennur too', '9fbc67', 23.45, 123, 456)
db.incAttr('6248fads', 'views', 5)
db.print_table()

# db.deleteVideoFromDB('6248fads')