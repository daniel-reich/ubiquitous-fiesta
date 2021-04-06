
def is_disarium(n):
  t = list(str(n))
  a = 0
  for i in range(len(t)):
    a += int(t[i])**(i+1)
    
  return a == n

