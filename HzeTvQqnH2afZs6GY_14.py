
def generateRug(n, direction):
  temp = []
  result = []
  if direction == 'left':
    for i in range(n):
      temp.append(i)
    for i in range(n):
      a = i
      t = []
      b = -1
      for j in range(n):
        t.append(temp[a])
        if a == 0:
          b = 1
        a += b
      result.append(t)
    return result
  else:
    for i in range(n-1,-1,-1):
      temp.append(i)
    for i in range(n):
      a = i
      t = []
      b = 1
      for j in range(n):
        t.append(temp[a])
        if a == n-1:
          b = -1
        a += b
      result.append(t)
    return result

