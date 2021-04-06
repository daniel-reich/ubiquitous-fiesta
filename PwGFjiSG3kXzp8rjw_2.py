
def chatroom_status(users):
  if not users:
    return "no one online"
  elif len(users) == 1:
    return "{} online".format(users[0])
  elif len(users) == 2:
    return '{} and {} online'.format(users[0], users[1])
  else:
    rest = len(users) - 2
    return '{}, {} and {} more online'.format(users[0], users[1], rest)

