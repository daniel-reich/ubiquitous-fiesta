
def chatroom_status(users):
  other=len(users)-2
  if len(users)==0:
    return "no one online"
  elif len(users)==1:
    return users[0] + " online"
  elif len(users)==2:
    return users[0] + " and " + users[1] + " online"
  elif len(users)>2:
    return users[0] + ", " + users[1] + " and " + str(other) + " more online"

