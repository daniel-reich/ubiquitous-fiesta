
def recaman(n):
  if n==0:
    return "---> Recaman's sequence: []\n---> Duplicates for n = 0: []"
  lst = [0]
  dup = []
  while len(lst)<n:
    if lst[-1]-len(lst) not in lst and lst[-1]-len(lst)>0:
      lst.append(lst[-1]-len(lst))
    else:
      lst.append(lst[-1]+len(lst))
    if lst.count(lst[-1])>1 and lst[-1] not in dup:
      dup.append(lst[-1])
  return "---> Recaman's sequence: "+str(lst)+"\n---> Duplicates for n = "+str(n)+": "+str(dup)

