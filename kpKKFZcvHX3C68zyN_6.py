
def swap_cards(n1, n2):
  m1, m2 = n1, n2
  
  if int(str(n1)[0]) > int(str(n1)[1]):
    n1 = int(str(n1)[0] + str(n2)[0])
    n2 = int(str(m1)[1] + str(m2)[1])
  else : 
    n1 = int(str(n2)[0] + str(n1)[1])
    n2 = int(str(m1)[0] + str(m2)[1])
​
  return n1 > n2

