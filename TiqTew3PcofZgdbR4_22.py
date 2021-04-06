
def bitwise_and(n1, n2):
  s1='{0:08b}'.format(n1)
  s2='{0:08b}'.format(n2)
  r=''.join(['1' if x=='1' and v=='1' else'0' for x,v in zip(s1,s2)])
  return int(r,2)
​
def bitwise_or(n1, n2):
  s1='{0:08b}'.format(n1)
  s2='{0:08b}'.format(n2)
  r=''.join(['1' if x=='1' or v=='1' else'0' for x,v in zip(s1,s2)])
  return int(r,2)
​
def bitwise_xor(n1, n2):
  s1='{0:08b}'.format(n1)
  s2='{0:08b}'.format(n2)
  r=''.join(['1' if (x=='1' or v=='1') and not (x=='1' and v=='1') 
  else'0' for x,v in zip(s1,s2)])
  return int(r,2)

