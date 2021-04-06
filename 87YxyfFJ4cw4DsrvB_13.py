
def generate_rug(n):
  h = range(n)
  rug = [[n//2]*n for i in h]
  for k in h[1:len(h)//2+1]:
    x = h[k:n-k]
    for i in h:
      for j in h:
        if i in x and j in x:
          rug[i][j] -= 1
  return rug

