
def lottery(ticket, win):
  miniwin=0
  for i in range(0,len(ticket)):
    for z in range(0,len(ticket[i][0])):
      if(ord(ticket[i][0][z])==ticket[i][1]):
        miniwin=miniwin+1
  if(miniwin>=win):
    return "Winner!"
  else:
    return "Loser!"
      #print (ticket[i][0][z])
      #print (ord(ticket[i][0][z]))

