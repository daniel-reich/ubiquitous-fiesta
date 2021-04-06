
def chatroom_status(users):
  if users:
    if len(users) == 1:
      return users[0] + " online"
    elif len(users) == 2:
      return "{} and {} online".format(users[0],users[1])
    else:
      return "{}, {} and {} more online".format(users[0],users[1],len(users)-2)
  else:
    return "no one online"

