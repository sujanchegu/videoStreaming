from video import *
class Playlist:
    def __init__(self):
        self.__num_of_vid = 0
        self.__playlist = set()

    def Add_To(self,vid_obj):
        self.__playlist.add(vid_obj)
        self.__num_of_vid += 1

    def Remove_From(self,vid_obj):
        self.__playlist.remove(vid_obj)
        self.__num_of_vid -= 1

    def Play_All(self):
        for vid in self.__playlist:
            vid.Play()

    def disp(self):
        for vid in self.__playlist:
            vid.disp()
