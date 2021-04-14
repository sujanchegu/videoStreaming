from dbase import *
from video import *

class History:
    def __init__(self,userid):
        self._personUID = userid
        # self._historyLIST = {}

    def add(self,vid_obj):
        # if(vid_obj not in self._historyLIST):
        #     self._historyLIST[vid_obj] = 1
        # else:
        #     self._historyLIST[vid_obj] += 1
        db.addVideoToHistory(vid_obj,self._personUID)


    def Search_History(self,name):
        recentViewed,mostViewed = db.retrieveHistory(self._personUID)
        #print(f"Recent viewed : {recentViewed}")
        for vid in recentViewed:
            #print(dir(vid))
            vid_name = db.retrieveParticularVideo(vid[0])[0]
            if(vid_name == name):
                return vid[0]
        return "404 : NOT FOUND"

    # def Delete_From_History(self,name):
    #     for vid in self._historyLIST:
    #         if(vid._Video__name == name):
    #             self._historyLIST.remove(vid)
    #             return "Deleted from history"
    #     return "404 : NOT FOUND"

    def Fetch_Ten(self):
        recentViewed,mostViewed = db.retrieveHistory(self._personUID)
        recentViewed_obj = []
        mostViewed_obj = []
        for vid in recentViewed:
            print("\n\nFetch_Ten : ",vid[0],"\n\n")
            vid_info =  db.retrieveParticularVideo(vid[0])
            vid_obj = Video(vid_info[0],vid_info[1],vid_info[-2],vid_info[2],vid_info[-3],vid_info[3],vid_info[4])
            recentViewed_obj.append(vid_obj)
        for vid in mostViewed:
            vid_info =  db.retrieveParticularVideo(vid[0])
            vid_obj = Video(vid_info[0],vid_info[1],vid_info[-2],vid_info[2],vid_info[-3],vid_info[3],vid_info[4])
            mostViewed_obj.append(vid_obj)

        # print("printing recent Viewed")
        # for i in recentViewed_obj:
        #     i.disp()
        # print("printing most Viewed")
        # for i in mostViewed_obj:
        #     i.disp()
        if(len(recentViewed_obj)<10):
            return recentViewed_obj
        else:
            return recentViewed_obj[0:10]




    def Erase_History(self):
        #self._historyLIST = {}
        db.removeHistory(self._personUID)
        return "Erased"



    # def disp(self):
    #     print("Displaying History: ")
    #     for vid in self._historyLIST:
    #         vid.disp()
