
def calculate(num1, num2, op):
    if op in "+-//%*" and isinstance(num1+num2,int):
      return eval(str(num1)+op+str(num2))

