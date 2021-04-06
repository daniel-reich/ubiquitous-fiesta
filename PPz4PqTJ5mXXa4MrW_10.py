
def ulam(n):
  
  hashtable = set([1,2])
  l = [1,2]
  for i in range(n-2):
    z = l[-1] + 1
    foundz = False
    while not foundz:
      c = 0
      for i in l:
        if z - i in hashtable and z - i != i:
          c += .5
          if c > 1:
            break
      else:
        if c > 0:
          foundz = True
          l.append(z)
          hashtable.add(z)
      z += 1
  return l[-1]

