
def society_name(friends):
  friends.sort()
  msg = ""
  for i in friends:
    msg = msg + i[0]
    
  return msg

