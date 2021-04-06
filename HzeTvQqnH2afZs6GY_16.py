
def generate_rug(n, direction):
  rug = list()
  for i in range(n):
    rug.append(list())
    for j in range(n)[::-1 if direction == 'right' else 1]: 
      rug[-1].append(abs(j-i))
  return rug

