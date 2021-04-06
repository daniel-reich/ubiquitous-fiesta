
class User:
  user_count = 0
  def __init__(self, user):
    self.user = user
    self.username = user
    User.user_count += 1

