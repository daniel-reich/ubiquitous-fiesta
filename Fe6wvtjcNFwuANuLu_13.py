
def ping_pong(lst, win):
  newlist = []
  for item in range(len(lst)-1):
    newlist += ["Ping!"]
    newlist += ["Pong!"]
  if win:
    newlist += ["Ping!"]
    newlist += ["Pong!"]
  else:
    newlist += ["Ping!"]
    
  return newlist

