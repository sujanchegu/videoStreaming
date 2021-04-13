from dbase import *

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
            temp_vid = db.FindSimilar(vid._Video__uri)
            self.vid_buffer.add(temp_vid)
        return self.vid_buffer
