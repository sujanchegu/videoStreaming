from history import *
from dbase import *

class Video:
    def __init__(self,name,uri,duration,desc,uid):
        self._name = name
        self._videoURI = uri
        self._duration = duration
        self._desc = desc
        self._likes = 0
        self._views = 0
        self._uid = uid

    def disp(self):
        print(f"name: {self._name}")
        print(f"uri: {self._videoURI}")
        print(f"duration: {self._duration}")
        print(f"description: {self._desc}")
        print(f"UID: {self._uid}")
        print(f"Likes: {self._likes}")
        print(f"Views: {self._views}")

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
