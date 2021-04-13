from video import *
class History:
    def __init__(self,userid):
        self._personUID = userid
        self._historyLIST = {}

    def add(self,vid_obj):
        if(vid_obj not in self._historyLIST):
            self._historyLIST[vid_obj] = 1
        else:
            self._historyLIST[vid_obj] += 1

    def Search_History(self,name):
        for vid in self._historyLIST:
            #print(dir(vid))
            if(vid._Video__name == name):
                return vid._Video__uri
        return "404 : NOT FOUND"

    def Delete_From_History(self,name):
        for vid in self._historyLIST:
            if(vid._Video__name == name):
                self._historyLIST.remove(vid)
                return "Deleted from history"
        return "404 : NOT FOUND"

    def Fetch_Ten(self):
        vid_obj_list = list(self._historyLIST.keys())
        if(len(vid_obj_list)>9):
            return vid_obj_list[0:11]
        else:
            return vid_obj_list

    def Erase_History(self):
        self._historyLIST = {}
        return "Erased"



    def disp(self):
        print("Displaying History: ")
        for vid in self._historyLIST:
            vid.disp()
