
def calculator(num1, operator, num2):
  ops={'+':(lambda x,y: x+y),'-':(lambda x,y: x-y),'/':(lambda x,y: x/y),'*':(lambda x,y: x*y)}
  if operator=='/' and num2==0:
    return "Can't divide by 0!"
  else:
    return ops[operator](num1,num2)

