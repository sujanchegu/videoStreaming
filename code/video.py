from history import *
from dbase import *

class Video:
    def __init__(self,name,uri,duration,desc,uid):
        self.__name = name
        self._videoURI = uri
        self.__duration = duration
        self.__desc = desc
        self.__likes = 0
        self.__views = 0
        self.__uid = uid

    def disp(self):
        print(f"name: {self.__name}")
        print(f"uri: {self._videoURI}")
        print(f"duration: {self.__duration}")
        print(f"description: {self.__desc}")
        print(f"UID: {self.__uid}")
        print(f"Likes: {self.__likes}")
        print(f"Views: {self.__views}")

    def Play(self,history):
        history.add(self)
        file_name = str(self._videoURI) + '.mp4'
        
    def Pause(self):
        None
    def Resume(self):
        None
    def Rewind(self):
        None
    def Forward(self):
        None
        