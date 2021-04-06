
def post_fix(expr):
  final = ''
  stack = []
  for i in expr.split():
    if i.isdigit():
      stack.append(i)
    else:
      res = str(stack[0]+i+stack[1])
      stack = [res]+stack[2:]
      final+=res
  return eval(res)

