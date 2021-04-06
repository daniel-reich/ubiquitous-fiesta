
class User:
    user_count = 0
    def __init__(self, username):
        self.username = username
        type(self).user_count += 1

