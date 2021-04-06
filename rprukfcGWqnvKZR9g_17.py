
class User:
  user_count = 0
  def __init__(self, name):
    self.username = name
    User.user_count += 1

