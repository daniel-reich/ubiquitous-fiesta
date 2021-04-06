
def ABA(s):
  c = [chr(x) for x in range(65, ord(s)+1)]
  a, i = '',0
  while i < len(c):
    a+= c[i] + a
    i+=1
  return a

