class recommeder:
    self.vid_buffer = []

    def Poll_History(self, user):
        recent_history = user._history.Fetch_Ten()
        return recent_history

    def send_updates(self, user):
        self.vid_buffer = db.calcSimilarity(self.Poll_History(user))
        return send_updates
