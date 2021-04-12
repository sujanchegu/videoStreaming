from datetime import datetime
import secrets
from history import *
from playlist import *
from collections import defaultdict

from video import *

class User:
    def __init__(self, userid = '', password = '',loginStatus = False , registerDate = ''):
        self._userid = userid
        self._password = password
        self._loginStatus = loginStatus
        self._registerDate = registerDate

    def register(self, id, pswd):
            self._userid = id
            self._password = pswd
            self._registerDate = datetime.now()

    def disp(self):
        print(f"{self._userid} {self._password} {self._registerDate}")


class Consumer(User):
    def __init__(self, consumer = None):
        if(consumer):
            self._consumerName = consumer._consumerName
            self._email = consumer._email
            self._history = consumer._history
            self._playlists = consumer._playlists
            User.__init__(self, consumer._userid, consumer._password, consumer._loginStatus, consumer._registerDate)
        else:
            self._consumerName = ''
            self._email = ''
            User.__init__(self)
            self._history = History(self._userid)
            self._playlists = defaultdict(lambda : Playlist())


    def register(self, name, email, password):
        self._consumerName = name
        self._email = email
        User.register(self, secrets.token_hex(nbytes=16), password)

    def ManageHistory(self, action = '', name_vid = ''):
        if(action == ''):
            print("Please provide an action :")
            print("1. search")
            print("2. delete")
            print("3. erase")

        elif(action == 'search'):
            if(name_vid == ''):
                print("Please provide name of video")
            else:
                return self._history.Search_History(name_vid)

        elif(action == 'delete'):
            if(name_vid == ''):
                print("Please provide name of video")
            else:
                return self._history.Delete_From_History(name_vid)
        elif(action == 'erase'):
                return self._history.Erase_History()

    # def Create_Playlist(self, name):
    #     self._playlists.append(Playlist(name))

    def Add_To_Playlist(self, playlist_name, vid):
        self._playlists[playlist_name].Add_To(vid)

    def Display_Playlist(self,playlist_name):
        self._playlists[playlist_name].disp()

    def Remove_From_Playlist(self, playlist_name, vid):
        self._playlists[playlist_name].Remove_From(vid)

    def Play_All_Playlist(self, playlist_name):
        self._playlists[playlist_name].Play_All()

    def disp(self):
        print(f"{self._consumerName} {self._email}", end = ' ')
        User.disp(self)


class Creator(Consumer):
    def __init__(self, cardno, consumer):
        self.__creditcardInfo = cardno
        Consumer.__init__(self, consumer)

    def Create_video(self, name,uri,duration,desc):
        return Video(name,uri,duration,desc, self._userid)

    def disp(self):
        print(f"{self.__creditcardInfo}", end = ' ')
        Consumer.disp(self)



consumer1 = Consumer()
consumer1.register('sriram', 'sriram@gmail.com', 'allahwhoakbar')
consumer1.disp()


creator1 = Creator('123', consumer1)
creator1.disp()

video1 = creator1.Create_video('mandalorian', '1', '58:00', 'awesome show' )

consumer2 = Consumer()
consumer2.register("Aditya", 'thecodeyoda', 'bitchassnigga')
consumer2.disp()

consumer2.Add_To_Playlist('favourites', video1)
consumer2.Play_All_Playlist('favourites')
consumer2.Display_Playlist('favourites')
