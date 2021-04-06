
import random
​
op = ["+", "-", "//", "*"]
​
def bf(s, target):
  global op
  if s.count("O")==0:
    if eval(s)==target:return s
    else:return None
  s = list(s)
  for i in range(4):
    idx = s.index("O")
    s[idx] = op[i]
    res = bf(''.join(s), target)
    if res!=None:return res
    s[idx] = "O"
    
​
def countdown(operands, target):
  operands = list(operands)
  while(1):
    s = 'O'.join(list(map(str,operands)))
    res = bf(s, target)
    if res!=None:return res
    random.shuffle(operands)

