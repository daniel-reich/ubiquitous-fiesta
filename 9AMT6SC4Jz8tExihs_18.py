
def generate_nonconsecutive(n):
  ret = []
  for i in range(2**n):
    temp = b(i)
    if '11' not in temp:
      ret.append(temp)
  l = max([len(i) for i in ret])
  ret = ['0'*(l-len(i))+i for i in ret]
  return ' '.join(ret)
    
def b(n):
  ret = ''
  while n>0:
    ret+=str(n%2)
    n//=2
  return ret[::-1] if ret else '0'

