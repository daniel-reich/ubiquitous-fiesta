
def pop(state):
  total = (len(state))
  center = round((len(state)-1) /2)
  lijst = []
​
  for i in range(center):
    lijst.append(i)
  for y in range(center, -1 ,-1):
    lijst.append(y)
  return(lijst)

