
#bit_rotate(8, 1, True) -> 4
# 8 in bin: 1000, rotated 1 step to the right: 0100, in dec: 4
def bit_rotate(n, m, d):
  b = bin(n)[2:]
  for i in range(0,m):
    if (d==True):
      b = b[-1:] + b[:-1]
    else:
      b =  b[1:] + b[:1]    
  return int(b, 2)
​
print (bit_rotate(283, 7, True), 110)

