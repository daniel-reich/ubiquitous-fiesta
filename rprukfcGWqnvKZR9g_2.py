
class User:
  user_count=0
  def __init__(self, u):
    self.username = u
    User.user_count += 1

