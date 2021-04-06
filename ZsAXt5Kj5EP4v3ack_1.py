
def secret(s):
  a = s.split('>')[0]
  b = s.split('>')[1].split('.')[0]
  c = s.split('.')[1].split('*')[0]
  d = int(s.split('*')[1])
  ret = '<'+a+'>'
  for i in range(1,d+1):
    ret+='<'+b+" class='"+c.split('$')[0]+('0'*(c.count('$')-1))+str(i)+"'></"+b+'>'
  ret+='</'+a+'>'
  return ret

