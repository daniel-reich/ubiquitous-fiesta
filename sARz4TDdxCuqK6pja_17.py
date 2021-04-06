
def infection(lst):
  nl = [''.join(r) for r in lst]
​
  for i in range(len(nl)):
    nl[i] = nl[i].replace('PV', 'VV')
    nl[i] = nl[i].replace('VP', 'VV')
​
  return [list(r) for r in nl]
​
​
def deadly_virus(lst, n):
​
  for _ in range(n):
    vi = list(map(list, zip(*infection(map(list, zip(*lst))))))
    oi = infection(lst)
​
    for r in range(len(lst)):
      for c in range(len(lst)):
        lst[r][c] = 'V' if 'V' in vi[r][c] + oi[r][c] else 'P'
​
  return lst

