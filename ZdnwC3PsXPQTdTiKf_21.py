
import operator
def calculator(num1, op, num2):
  ops = { "+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul} 
  if op == '/' and num2==0:
    return 'Can\'t divide by 0!'
  return ops[op](num1,num2)

