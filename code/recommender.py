class Recommender:
    def __init__(self):
        self.vid_buffer = []

    def Poll_History(self, user):
        recent_history = user._history.Fetch_Ten()
        return recent_history

    def send_updates(self, user):
        recent_history = self.Poll_History(user)

        for vid in recent_history:
            temp_vid = db.FindSimilar(vid)

        return send_updates
