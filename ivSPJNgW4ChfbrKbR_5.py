
def soroban(frame):
  fives = frame[1]
  lists = [[] for i in range(5)]
  cols = [[] for _ in range(7)]
  fiss = []
  for i in fives:
      if i == 'O':
        fiss.append(5)
      else:
        fiss.append(0)
  for a,fram in enumerate(frame[3:]):
    for i in fram:
      if i=='O':
        lists[a].append(1)
      else:
        lists[a].append(0)
  for i in lists:
    for ii,numb in enumerate(i):
      cols[ii].append(numb)
  lower =[]
  for i in cols:
    lower.append(sum(i[:i.index(0)]))
  res = str()
  for i,j in zip(fiss,lower):
    res = res+str(i+j)
  return(int(res))

