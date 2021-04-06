
import operator
from collections import deque
op_map = {'+' : operator.add,
          '-' : operator.sub,
          '*' : operator.mul,
          '/' : operator.truediv}
​
def postfix(stack):
  if isinstance(stack, str):
    stack = deque([int(x) if x.isdigit() else x for x in stack.split()])
  op = stack.pop()
  if isinstance(op, int) or isinstance(op, float):
    return op
  else:
    arg2 = postfix(stack)
    arg1 = postfix(stack)
    return op_map[op](arg1, arg2)

