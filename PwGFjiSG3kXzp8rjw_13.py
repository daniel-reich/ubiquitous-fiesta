
def chatroom_status(users):
  if users == []:
    return "no one online"
  elif len(users) == 1:
    return users[0]+ " online"
  elif len(users) == 2:
    return users[0] + " and "+ users[1] + " online"
  else:
    n = len(users)-2
    return users[0] + ", "+ users[1] + " and " + str(n) + " more online"
