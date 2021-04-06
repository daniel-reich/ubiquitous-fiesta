
def ping_pong(lst, win):
  for x in range(len(lst)-1,0,-1): lst.insert(x,"Pong!")
  return lst if not win else lst + ["Pong!"]

