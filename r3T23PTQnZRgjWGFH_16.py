
import operator
def operate(n1,n2,o):
  ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  
    '%' : operator.mod,
    '^' : operator.xor,
    }
    
  return ops[o](n1,n2)

