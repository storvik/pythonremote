# Class for sending notifications
class Notification:
    def __init__(self, key, sender, title, message):
        self.key = key
        self.sender = sender
        self.title = title
        self.text = message
