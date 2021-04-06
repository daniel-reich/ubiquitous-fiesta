
def calculate(num1, num2, op):
  if op=='+':
    answer=num1+num2
  elif op=='-':
    answer=num1-num2
  elif op=='*':
    answer=num1*num2
  elif op=='//':
    answer=num1//num2
  elif op=='/':
    answer=num1/num2
  elif op=='%':
    answer=num1%num2
  return answer

