
def atbash(txt):
​
  lowerkey = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
  lowerval = reversed(lowerkey)
​
  lv2 = []
​
  for item in lowerval:
    lv2.append(item)
  
  lowerval = lv2
  del lv2
  lower = {}
​
  for n in range(0, len(lowerkey)):
    key = lowerkey[n]
    val = lowerval[n]
​
    lower[key] = val
  
  upperkey = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.upper().split()
  upperval = reversed(upperkey)
​
  uv2 = []
​
  for item in upperval:
    uv2.append(item)
  
  upperval = uv2
  del uv2
  upper = {}
​
  for n in range(0, len(upperkey)):
    k = upperkey[n]
    v = upperval[n]
​
    upper[k] = v
​
  ns = ''
​
  for item in txt:
    if item in upper.keys():
      ns += upper[item]
    elif item in lower.keys():
      ns += lower[item]
    else:
      ns += item
    
  return ns

