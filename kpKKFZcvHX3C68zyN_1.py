
def swap_cards(n1, n2):
  n1, n2 = [[int(i) for i in list(str(n))] for n in [n1, n2]]
​
  if n1[0] == n1[1]:
    i = 0
  else:
    i = n1.index(min(n1))
    
  n1[i], n2[0] = n2[0], n1[i]
  return n1 > n2

