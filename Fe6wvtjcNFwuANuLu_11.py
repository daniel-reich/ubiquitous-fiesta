
def ping_pong(lst, win):
  pingpong=[]
  eyes=len(lst)-1
  counter=0
  if win == False:
    for x in lst:
      if counter == eyes:
        pingpong.append(x)
      else:
        counter+=1
        pingpong.append(x)
        pingpong.append("Pong!")
    return pingpong
  else:
    for x in lst:
      pingpong.append(x)
      pingpong.append("Pong!")
    return pingpong

