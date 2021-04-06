
def eratosthenes(num):
  if num == 1 or num == 0:
    return []
  l = [True]*num
  l.insert(0,0)
  l[1] = False
  i = 2
  while i <= num:
    if l[i] == True:
      for j in range(i+1, num+1):
        if j%i == 0:
          l[j] = False
    i += 1
​
  p = []
  for i in range(len(l)):
    if l[i] == True:
      p.append(i)
  return p

