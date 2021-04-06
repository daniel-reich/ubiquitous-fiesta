
def chatroom_status(users):
  if users:
    if len(users) == 1:
      return users[0] + " online"
    if len(users) == 2:
      return users[0] + " and " + users[1] + " online"
    else:
      return users[0] + ", " + users[1] + " and " + str(len(users)-2) + " more online"
  return "no one online"
