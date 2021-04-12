import sqlite3
from sqlite3 import Error

class DBase():
    def __init__(self):
        self.__conn = None
        try:
            self.__conn = sqlite3.connect('../assets/database.db')
            
            self.__conn.execute('DROP TABLE videos')
            self.__conn.execute('CREATE TABLE videos (name TEXT, uri TEXT,\
            desc TEXT, likes INTEGER, views INTEGER, path BLOB, \
            uid TEXT, dur REAL)')

            self.__conn.execute('DROP TABLE users')
            self.__conn.execute('CREATE TABLE users (name TEXT, email TEXT,\
            uid TEXT, passwd TEXT, regDate TEXT, creditCard TEXT,\
            isCreator INTEGER)')

        except Error as e:
            print(e)

    def deleteVideoFromDB(self, iURI):
        try:
            self.__conn.execute('DELETE FROM videos WHERE {condition}',
            condition = 'uri = ' + iURI)
        except Error as e:
            print(e)

    def calcSimilarity(self, iURI1, iURI2):
        pass
    
    def incAttr(self, iURI, attr, count=1):
        try:
            self.__conn.execute(f'UPDATE videos SET {bute} = {bute} \
            + {cnt} WHERE {condition}', bute=attr,
            cnt = count, condition='uri = ' + iURI)
        except Error as e:
            print(e)

    def regUser(self, iName, iEmail, iUID, iPassword, iRegDate, iCCard, iIsCreator):
        try:
            self.__conn.execute('INSERT INTO users VALUES {name}, {email},\
            {uid}, {passwd}, {regDate}, {creditCard}, {isCreator}',
            name=iName, email=iEmail, uid=iUID, passwd=iPassword,
            regDate=iRegDate, creditCard=iCCard, isCreator=iIsCreator)
        except Error as e:
            print(e)

    def regCreator(iUID):
        try:
            self.__conn.execute('UPDATE users SET isCreator = 1 WHERE {condition}',
            condition = 'uid = '+iUID)
        except Error as e:
            print(e)


db = DBase()
