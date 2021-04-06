
import math
def find_vertex(x):
  a1 = x.split('x')[0]
  b1 = x.split('x')[1]
  a = int(''.join([i for i in a1 if i.isdigit()]))
  b = int(''.join([i for i in b1 if i.isdigit()]))
  
  if b1.strip()[0]=='+' and a1[0].isdigit():
    return -math.ceil(b / (2*a))
  else:
    return (b // (2*a))

