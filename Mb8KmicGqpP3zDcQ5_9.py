
def josephus(n, skip):
  tab = create(n)
  skip -= 1
  idx = skip
  while len(tab) > 1:
    tab.pop(idx)
    idx = (idx + skip) % len(tab)
  return tab[0]
​
def create(n):
  tab = []
  for x in range(0, n):
    tab.append(x+1) 
  return tab

