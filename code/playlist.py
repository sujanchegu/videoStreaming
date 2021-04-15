from video import *
from history import *
from dbase import *

class Playlist:
    def __init__(self, name, email):
        # self._num_of_vid = 0
        # self._playlist = set()
        self._name = name;
        self._email = email;
        # db.createPlaylist(email, name);
        x = db.retrievePlaylist(email, name)
        if(x == None):
            db.createPlaylist(email, name)

    def Add_To(self,vid_obj):
        # self._playlist.add(vid_obj)
        # self._num_of_vid += 1
        db.addToPlaylist(self, vid_obj)

    def Remove_From(self,vid_obj):
        # self._playlist.remove(vid_obj)
        # self._num_of_vid -= 1
        db.removeFromPlaylist(self, vid_obj)

    def Play_All(self,history):
        # for vid in self._playlist:
        #     vid.Play(history)
        playlist = db.retrievePlaylist(self._email,self._name)
        print(f"playlist : {playlist}")
        for i in playlist:
            vid_info = db.retrieveParticularVideo(i[0])
            print("\n\nvid_info in Play_All : ",vid_info, "\n\n")
            #('sriram eating', 'video1', 'bennur too', 123, 501, 'abc@gmail.com', 23.45)
            vid_obj = Video(vid_info[0],vid_info[1],vid_info[-2],vid_info[2],vid_info[-3],vid_info[3],vid_info[4])
            vid_obj.Play(history)

    def disp(self):
        playlist = db.retrievePlaylist(self._email,self._name)
        #print(f"playlist : {playlist}")
        for i in playlist:
            vid_info = db.retrieveParticularVideo(i[0])
            vid_obj = Video(vid_info[0],vid_info[1],vid_info[-2],vid_info[2],vid_info[-3],vid_info[3],vid_info[4])
            vid_obj.disp()
