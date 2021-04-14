from dbase import *

class topVideosRecommender:
    def __init__(self):
        self._mostViewed = []
        self._mostLiked = []
        self._recentlyUpload = []

    def retrieveFromDB(self):
        topVideos = db.retrieveTopVideos()
        self._recentlyUpload = topVideos[0]
        self._mostLiked = topVideos[1]
        self._mostViewed = topVideos[2]

    def getTopVideos(self):
        self.retrieveFromDB()
        return (self._mostViewed, self._mostLiked, self._recentlyUpload)

    
obj = topVideosRecommender()