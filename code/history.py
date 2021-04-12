from video import *
class History:
    def __init__(self,userid):
        self.__uid = userid
        self.__history = {}

    def add(self,vid_obj):
        if(vid_obj not in self.__history):
            self.__history[vid_obj] = 1
        else:
            self.__history[vid_obj] += 1

    def Search_History(self,name):
        for vid in self.__history:
            #print(dir(vid))
            if(vid._Video__name == name):
                return vid._Video__uri
        return "404 : NOT FOUND"

    def Delete_From_History(self,name):
        for vid in self.__history:
            if(vid._Video__name == name):
                self.__history.remove(vid)
                return "Deleted from history"
        return "404 : NOT FOUND"

    def Erase_History(self):
        self.__history = {}
        return "Erased"

    

    def disp(self):
        print("Displaying History: ")
        for vid in self.__history:
            vid.disp()
    
