
def calculator(a, op, b):
  return {
    '+': a + b,
    '-': a - b,
    '//': a / b,
    '*': a * b,
  }[op]
​
import re
​
def prefix(exp):
  lst =  exp.replace('/', '//').split(' ')[::-1]
  res = []
  for i in lst:
    if bool(re.match(r'^-?\d+$', i)):
      res.append(i)
    else:
      res.append(calculator(int(res.pop()), i, int(res.pop())))
  return res[0]

