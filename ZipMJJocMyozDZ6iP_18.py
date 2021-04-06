
import math
​
def group(l, s):
  if len(l) % s == 0:
    x = int(len(l)/s)
  elif len(l) % s == 1:
    x = int((len(l)/s)) + 1
  else:
    if (len(l) % (len(l)%s)) == 0:
      x = int((len(l)/s)) + 1
      s = s-1
    else:
      x = int(math.ceil(len(l)/float(s)))
    
  out = []
  
  for i in range(x):
    if (len(out) != 0) and ((len(l)-(len(out)*s))<s):
      s = len(l)%s
    else:
      s = s
  
    temp = [l[i]]
    for j in range(1, s):
      temp.append(l[i+(j*x)])
    out.append(temp)
  
  return out

