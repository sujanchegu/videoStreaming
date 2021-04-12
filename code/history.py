from video import *
class History:
    def __init__(self,userid):
        self.__uid = userid
        self.__history = set()

    def add(self,vid_obj):
        self.__history.add(vid_obj)

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
        self.__history = set()
        return "Erased"

    def disp(self):
        print("Displaying History: ")
        for vid in self.__history:
            vid.disp()
    
