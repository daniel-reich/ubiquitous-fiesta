
def primorial(n):
  if n==1: return 2
  a = []
  for i in range(2, n**2):
    for j in range(2, i):
      if i%j==0:
        break
    else: a.append(i)
  return eval("*".join(str(i) for i in a[:n]))

