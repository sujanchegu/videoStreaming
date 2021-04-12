class History:
    def __init__(self,userid):
        self.__history = set()

    def add(self,vid_obj):
        self.__history.add(vid_obj)

    def Search_History(self,name):
        for vid in self.__history:
            if(vid.__name == name):
                return vid.__uri

    def Delete_From_History(self,name):
        for vid in self.__history:
            if(vid.__name == name):
                self.__history.remove(vid)

    def Erase_History(self):
        self.__history = set()
