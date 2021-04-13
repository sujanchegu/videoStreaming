from dbase import *
from video import *
class Recommender:
    def __init__(self):
        self.vid_buffer = set()

    def Poll_History(self, user):
        recent_history = user._history.Fetch_Ten()
        return recent_history

    def update(self, user):
        recent_history = self.Poll_History(user)
        self.vid_buffer.clear()
        for vid in recent_history:
            temp_vid = db.FindSimilar(vid._videoURI, (vid._duration, vid._likes, vid.views))
            name,uri,duration,desc,uid, likes = 0, views = 0
            temp_vid = Video(temp[0], temp[1], temp[6],temp[2], temp[5], temp[3], temp[4])
            self.vid_buffer.add(temp_vid)
        return self.vid_buffer
