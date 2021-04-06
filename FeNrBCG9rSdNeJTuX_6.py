
def max_possible(n1, n2):
  n1 = [int(x) for x in str(n1)] 
  n2 = [int(x) for x in str(n2)] 
​
  for i, num in enumerate(n1):
    if num < max(n2):
      j = n2.index(max(n2))
      n1[i] = n2[j]
      n2[j] = 0
      
  vysledok = 0
  i = 0
  
  n1.reverse()
  
  for x in n1:
    vysledok = vysledok + x*10**i
    i += 1
    
  return vysledok

