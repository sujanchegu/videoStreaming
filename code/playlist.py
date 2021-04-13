from video import *
from history import *
from dbase import *

class Playlist:
    def __init__(self, name, email):
        self._num_of_vid = 0
        self._playlist = set()
        self._name = name;
        self._email = email;
        db.createPlaylist(email, name);

    def Add_To(self,vid_obj):
        self._playlist.add(vid_obj)
        self._num_of_vid += 1
        db.addToPlaylist(self, vid_obj)

    def Remove_From(self,vid_obj):
        self._playlist.remove(vid_obj)
        self._num_of_vid -= 1
        db.removeFromPlaylist(self, vid_obj)

    def Play_All(self,history):
        for vid in self._playlist:
            vid.Play(history)

    def disp(self):
        for vid in self._playlist:
            vid.disp()
