
def flipping_bits(n):
  b = d_to_b(n)
  b = [1 if i==0 else 0 for i in b]
  return b_to_d(b)
  
def d_to_b(n):
  ret = []
  while n>0:
    ret.append(n%2)
    n//=2
  ret+=[0]*(32-len(ret))
  return ret
  
def b_to_d(b):
  ret = 0
  for i in range(len(b)):
    ret+=(2**i)*b[i]
  return ret

