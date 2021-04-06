
def chatroom_status(users):
  result=""
  if len(users)==0:
    result="no one online"
  elif len(users)==1:
    result=users[0]+" online"
  elif len(users)==2:
    result=users[0]+" and "+users[1]+" online"
  else:
    result=users[0]+", "+users[1]+" and "+str(len(users)-2)+" more online"
  return result

