
def chatroom_status(users):
  if users == []:
    return "no one online"
  a = ' and '.join(users)
  if len(users) > 2:
    a = users[0] +", " + users[1] +" and " + str(len(users)-2) + " more"
  
  return a + " online"

