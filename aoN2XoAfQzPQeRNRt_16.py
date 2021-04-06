
def operation(a, b, op):
  a = int(a)
  b = int(b)
  if (op=="divide" and b==0):
    return "undefined"
  else:
    if(op=="add"):
      i=a+b
      return str(round(i))
    elif(op=="subtract"):
      i=a-b
      return str(round(i))
    elif(op=="multiply"):
      i=a*b
      return str(round(i))
    else:
      i=a/b
      return str(round(i))

