
def eratosthenes(num):
  if num<2: return []
  elif num == 2: return [2]
  else:
    sv = [2]
    for x in range(3, num+1):
      sv.append(x)
      for y in range(2,x):
        if x%y==0:
          sv.pop()
          break
  return sv

