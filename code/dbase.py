import os
import re
import sqlite3
from sqlite3 import Error
from scipy import spatial

class DBase:
    def __init__(self):
        self.__conn = None
        try:
            # os.system('rm ../assets/database.db')
            # os.system('touch ../assets/database.db')

            self.__conn = sqlite3.connect('../assets/database.db', check_same_thread=False)

            self.__conn.execute('''CREATE TABLE videos (name TEXT, uri TEXT,
            desc TEXT, likes INTEGER, views INTEGER, email TEXT, dur REAL, uploadDate TEXT)''')

            self.__conn.execute('''CREATE TABLE users (name TEXT, email TEXT CONSTRAINT email_is_pkey PRIMARY KEY,
            passwd TEXT, regDate TEXT, creditCard TEXT, isCreator INTEGER)''')
        except Error as e:
            print("dbase::__init__", e)



    def addVideo(self, iName, iURI, iDesc, iEmail, iDur, iUploadDate, iLikes=0, iViews=0):
        try:
            params = (iName, iURI, iDesc, iLikes, iViews, iEmail, iDur, iUploadDate)
            self.__conn.execute('INSERT INTO videos VALUES (?, ?, ?, ?, ?, ?, ?, ?)', params)
            self.__conn.commit()
        except Error as e:
            print("dbase::addVideo", e)

    def deleteVideo(self, iURI):
        try:
            self.__conn.execute(f'DELETE FROM videos WHERE uri = "{iURI}"')
            os.remove("../assets/videos/" + iURI + '.mp4')
            self.__conn.commit()
        except Error as e:
            print("dbase::deleteVideo", e)

    def retrieveUploadedVideos(self, iEmail):
        try:
            csor = self.__conn.cursor()
            csor.execute(f'SELECT * FROM videos WHERE email = "{iEmail}"')
            return csor.fetchall()
        except Error as e:
            print("dbase::retrieveUploadedVideos")

    def retrieveParticularVideo(self, iURI):
        try:
            csor = self.__conn.cursor()
            csor.execute(f'SELECT * FROM videos WHERE uri = "{iURI}"')
            res = csor.fetchall()
            print("\n\ncsor.fetchall in retrieveParticularVideo : ", iURI, res[0],"\n\n")
            return res[0]
        except Error as e:
            print("dbase::retrieveParticularVideo", e)

    def retrieveAllVideos(self):
        try:
            csor = self.__conn.cursor()
            csor.execute(f'SELECT * FROM videos')
            return csor.fetchall()
        except Error as e:
            print("dbase::retrieveAllVideos", e)

    def FindSimilar(self, iURI, inp_vector):
        try:
            csor = self.__conn.cursor()
            csor.execute(f'SELECT uri,dur, likes, views FROM videos WHERE uri != "{iURI}"')
            vectors = csor.fetchall()
            store = {}
            print("\n\nVectors in FindSimilar : ", vectors,"\n\n")
            for vector in vectors:
                store[vector[0]] = [float(vector[1]), float(vector[2]), float(vector[3])]
            min  = 1.0
            ret_uri = ''
            for vid in store:
                temp = spatial.distance.cosine(inp_vector, store[vid])
                if(temp < min):
                    min = temp
                    ret_uri = vid

            csor2 = self.__conn.cursor()
            csor2.execute(f'SELECT * FROM videos WHERE uri = "{ret_uri}"')
            return csor2.fetchall()[0]

        except Error as e:
            print("dbase::incAttr", e)
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

    def retrieveUser(self, iEmail):
        try:
            csor = self.__conn.cursor()
            csor.execute(f'SELECT * FROM users WHERE email = "{iEmail}"')
            record = csor.fetchall()
            csor.close()
            return record[0]
        except Error as e:
            print("dbase::retrieveUser", e)

    def changeUserDetails(self, iEmail, **kwargs):
        # email change is not allowed
        # Keys allowed in kwargs along with types are:
            # name TEXT,
            # passwd TEXT,
            # creditCard TEXT,
            # isCreator INTEGER
        try:
            kwargs.pop('email', None)
            kwargs.pop('regDate', None)
            if ('isCreator' in kwargs.keys()):
                self.__conn.execute(f'UPDATE users SET isCreator = {kwargs["isCreator"]} WHERE email = "{iEmail}"')
                del kwargs['isCreator']
            for iAttr, iAttrValue in kwargs.items():
                self.__conn.execute(f'UPDATE users SET {iAttr} = "{iAttr}" WHERE email = "{iEmail}"')
            self.__conn.commit()
        except Error as e:
            print("dbase::changeUserDetails", e)

    def checkCreator(self, iEmail):
        try:
            return (self.retrieveUser(iEmail)[5] == 1)
        except Error as e:
            print("dbase::checkCreator", e)



    # def addHistory(self, iHistoryObject):
    #     try:
    #         iEmail = iHistoryObject._personUID
    #         csor = self.__conn.cursor()
    #         csor.execute(f'SELECT MAX(session) FROM [{iEmail}]')
    #         iSessionNo = csor.fetchall()[0][0]
    #         if (iSessionNo == None):
    #             iSessionNo = 1
    #         else:
    #             iSessionNo = iSessionNo + 1
    #         for iVideoObject,iCount in iHistoryObject._historyLIST.items():
    #             iURI = iVideoObject._videoURI
    #             csor.execute(f'SELECT EXISTS (SELECT 1 FROM [{iEmail}] WHERE uri ="{iURI}")')
    #             if(csor.fetchall()[0][0] == 0):
    #                 self.__conn.execute(f'INSERT INTO [{iEmail}] values (?, ?, ?)', (iURI, iCount, iSessionNo))
    #             else:
    #                 self.__conn.execute(f'UPDATE [{iEmail}] SET count = count + {iCount} WHERE uri = "{iURI}"')
    #                 self.__conn.execute(f'UPDATE [{iEmail}] SET session = {iSessionNo} WHERE uri = "{iURI}"')
    #         csor.close()
    #         self.__conn.commit()
    #     except Error as e:
    #         print("dbase::addHistory", e)

    def addVideoToHistory(self, iVideoObject, iEmail):
        try:
            csor = self.__conn.cursor()
            csor.execute(f'SELECT MAX(session) FROM [{iEmail}]')
            iSessionNo = csor.fetchall()[0][0]
            if (iSessionNo == None):
                iSessionNo = 1
            else:
                iSessionNo = iSessionNo + 1
            iURI = iVideoObject._videoURI
            iCount = 1
            csor.execute(f'SELECT EXISTS (SELECT 1 FROM [{iEmail}] WHERE uri ="{iURI}")')
            if(csor.fetchall()[0][0] == 0):
                    self.__conn.execute(f'INSERT INTO [{iEmail}] values (?, ?, ?)', (iURI, iCount, iSessionNo))
            else:
                    self.__conn.execute(f'UPDATE [{iEmail}] SET count = count + {iCount} WHERE uri = "{iURI}"')
                    self.__conn.execute(f'UPDATE [{iEmail}] SET session = {iSessionNo} WHERE uri = "{iURI}"')
        except Error as e:
            print("dbase::addVideoToHistory", e)


    def retrieveHistory(self, iEmail):
        try:
            csor = self.__conn.cursor()
            csor.execute(f'SELECT * FROM [{iEmail}] ORDER BY session DESC')
            recentViewed = csor.fetchmany(10)
            csor.execute(f'SELECT * FROM [{iEmail}] ORDER BY count DESC')
            mostViewed = csor.fetchmany(10)
            return (recentViewed, mostViewed)
        except Error as e:
            print("dbase::retrieveHistory", e)

    def removeHistory(self, iEmail):
        try:
            self.__conn.execute(f'DROP TABLE [{iEmail}]')
            self.__conn.execute(f'CREATE TABLE [{iEmail}] (uri TEXT, count INTEGER, session INTEGER)')
            self.__conn.commit()
        except Error as e:
            print("dbase::removeHistory", e)




    def createPlaylist(self, iEmail, iPlaylistName):
        try:
            self.__conn.execute(f'CREATE TABLE [{iEmail + iPlaylistName}] (uri TEXT)')
            self.__conn.commit()
        except Error as e:
            print("dbase::createPlaylist", e)

    def addToPlaylist(self, iPlaylist, iVideoObject):
        try:
            iEmail = iPlaylist._email
            iPlaylistName = iPlaylist._name
            iURI = iVideoObject._videoURI
            csor = self.__conn.cursor()
            csor.execute(f'SELECT EXISTS (SELECT 1 FROM [{iEmail + iPlaylistName}] WHERE uri ="{iURI}")')
            if(csor.fetchall()[0][0] == 0):
                self.__conn.execute(f'INSERT INTO [{iEmail + iPlaylistName}] VALUES (?)', (iURI,))
                self.__conn.commit()
        except Error as e:
            print("dbase::addToPlaylist", e)

    def removeFromPlaylist(self, iPlaylist, iVideoObject):
        try:
            iPlaylistName = iPlaylist._name
            iEmail = iPlaylist._email
            iURI = iVideoObject._videoURI
            self.__conn.execute(f'DELETE FROM [{iEmail + iPlaylistName}] where uri = "{iURI}"')
            self.__conn.commit()
        except Error as e:
            print("dbase::removeFromPlaylist", e)

    def retrievePlaylist(self, iEmail, iPlaylistName):
        try:
            csor = self.__conn.cursor()
            csor.execute(f'SELECT * FROM [{iEmail + iPlaylistName}]')
            return csor.fetchall()
        except:
            print("dbase::retrievePlaylist", e)

    def retrieveListOfPlaylists(self, iEmail):
        try:
            csor = self.__conn.cursor()
            csor.execute('.tables')
            returnList = []
            for table in csor.fetchall():
                if (re.match('^' + iEmail, table)):
                    returnList.append(table)
            return returnList
        except Error as e:
            print("dbase::retrieveListOfPlaylists", e)

 # def __del__(self):
    #     os.system('rm ../assets/database.db')







    #DEBUG SHIT
    def print_table(self, iName):
        csor = self.__conn.cursor()
        # if ('@' in iName):
        #     csor.execute(f'SELECT * from [{iName}]')
        # else:
        #     csor.execute(f'SELECT * from {iName}')
        csor.execute(f'SELECT * from {iName}')
        print(csor.fetchall())

db = DBase()
