class tweet(object):
    def __init__(self):
        self.id = None
        self.parent_id = None
        self.time = None
        self.likes = None
        self.replies = None
        self.retweets = None
        self.text = None

    def _initialize(self, data):
        self.id = str(data[0])
        self.parent_id = str(data[1])
        self.time = str(data[2])
        self.likes = str(data[3])
        self.replies = str(data[4])
        self.retweets = str(data[5])
        self.text = str(data[6])
    def _get_dic(self):
        response = {}
        response["id"] = self.id
        response["pid"] = self.parent_id
        response["time"] = self.time
        response["likes"] = self.likes
        response["replies"] = self.replies
        response["retweets"] = self.retweets
        response["text"] = self.text
        return response