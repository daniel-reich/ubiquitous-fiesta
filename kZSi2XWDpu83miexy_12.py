
def post_fix(ops):
  ops = ops.split()
​
  while len(ops) > 1:
    i = 0
    while ops[i] not in '+-*/':
      i += 1
​
    op = ops.pop(i)
    n1 = ops.pop(0)
    n2 = ops.pop(0)
​
​
    ops.insert(0, str(eval(n1 + op + n2)))
​
  return eval(ops[0])

