import sqlite3
from sqlite3 import Error

class DBase():
    def __init__(self):
        __conn = None
        try:
            __conn = sqlite3.connect('../assets/database.db')
            __conn.execute('DROP TABLE videos')
            __conn.execute('CREATE TABLE videos (name TEXT, uri TEXT,\
            desc TEXT, likes INTEGER, views INTEGER, path BLOB, \
            uid TEXT, dur REAL)')
        except Error as e:
            print(e)

    def saveToDB(self):
        pass

    def deleteFromDB(self, vid_uri):
        try:
            __conn.execute('DELETE FROM {table} WHERE {condition}',
            table = 'videos', condition = 'uri = ' + vid_uri)
        except Error as e:
            print(e)

    def calcSimilarity(self, vid_uri1, vid_uri2):
        pass
    
    def incAttr(self, vid_uri, attr, count=1):
        try:
            self.__conn.execute(f'UPDATE {table} SET {bute} = {bute} \
            + {cnt} WHERE {condition}', table='videos', bute=attr,
            cnt = count, condition='uri = ' + vid_uri)
        except Error as e:
            print(e)

    def retreive_videopath(self, vid_uri):
        try:
            cur = self.__conn.cursor()
            path = cur.execute("SELECT path FROM {_table} WHERE \
            {condition}", _table = 'videos', condition = 'uri = ' + vid_uri)
            return path
        except Error as e:
            print(e)

db = DBase()
