
def josephus(n,m):
  l = []
  listOfMen=[]
  for i in range(1,n+1):
    listOfMen.append(i)
  turn=0
  addition = n
  k = 0
  division = 0
  dell = []
  minus2 = 0
  nextvar = 0
  dell1 = []
  while True:
    # Checking 
    if len(listOfMen) == 1:
      return listOfMen[0]
      break;
​
    # m=1 state
    if m == 1:
      return listOfMen[-1]
      break;
​
    # n>=m state
    if len(listOfMen) >= m:
      # First circle
      if turn == 0:
        for i in range(m,len(listOfMen)+1,m):
          dell1.append(listOfMen[i-1])
          k = i
​
      # After first circle
      else:
        for i in range(minus,len(listOfMen)+1,m):
          dell[turn].append(listOfMen[i-1])
          k = i
​
      # First circle delletion
      if turn == 0:
        dell.append(dell1)
​
      # After first cirlce delletion
      dell.append([])
      minus = m-(len(listOfMen)-k)
​
      # Removing from main list
      for d in dell[turn]:
        listOfMen.remove(d)
​
    # n<m state
    else:
      division = m%len(listOfMen)
      if minus != 0:
        if minus-1 > len(listOfMen)-1:
          dell[turn].append(listOfMen[0])
          minus2 = 0
          for d in dell[turn]:
            listOfMen.remove(d)
          dell.append([])
          minus = 0
        else:
          dell[turn].append(listOfMen[minus-1])
          minus2 = minus-1
          for d in dell[turn]:
            listOfMen.remove(d)
          dell.append([])
          minus = 0
      else:
        nextvar = minus2+(division-1)
        if nextvar>len(listOfMen)-1:
          nextvar = nextvar - len(listOfMen)
          dell[turn].append(listOfMen[nextvar])
          minus2 = nextvar
          for d in dell[turn]:
            listOfMen.remove(d)
          dell.append([])
        else:
          dell[turn].append(listOfMen[nextvar])
          minus2 = nextvar
          for d in dell[turn]:
            listOfMen.remove(d)
          dell.append([])
      if len(listOfMen) == 1:
        return listOfMen[0]
        break;
​
    # New turn
    turn += 1

