
def bell(n):
  if n<3: return n
  t = [1, 2]
  for _ in range(n-2):
    temp=[t[-1]]
    for i in range(len(t)):
      temp.append(temp[-1]+t[i])
    t=temp
  return t[-1]

