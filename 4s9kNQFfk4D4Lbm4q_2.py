
def ABA(s):
  p = ''
  for i in range(65,ord(s)+1): 
    p = p + chr(i) + p
  return p

