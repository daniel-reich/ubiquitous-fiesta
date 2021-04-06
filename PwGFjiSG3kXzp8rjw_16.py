
def chatroom_status(users):
  return "no one online" if not users else "{} online".format(users[0]) if len(users) == 1 else "{} and {} online".format(users[0], users[1]) if len(users) == 2 else "{}, {} and {} more online".format(users[0], users[1], len(users) - 2)

