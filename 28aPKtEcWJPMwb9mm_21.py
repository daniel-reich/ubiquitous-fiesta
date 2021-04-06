
def modify(txt):
  a=' abcdefghijklmnopqrstuvwxyz'
  return int(d_b(int(''.join([str(a.index(i)) for i in txt[::-1]]))))
def d_b(n):
  ret = ''
  while n>0:
    ret+=str(n%2)
    n//=2
  return ret[::-1]

