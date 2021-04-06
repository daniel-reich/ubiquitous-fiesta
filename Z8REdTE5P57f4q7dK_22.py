
def collatz(n):
  a = [n]
  while a[-1] != 1:
    l = a[-1]
    if l%2 == 0:
      a.append(l/2)
    elif l%2 != 0:
      a.append(l*3+1)
  
    
  
  return (len(a), max(a))

