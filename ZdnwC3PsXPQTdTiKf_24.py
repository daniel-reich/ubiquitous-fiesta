
def calculator(num1, operator, num2):
  try:
    if operator == '+':
      return num1+num2
    if operator == '-':
      return num1-num2
    if operator == '*':
      return num1*num2
    if operator == '/':
      return num1//num2
  except ZeroDivisionError:
    if num2 == 0:
      return "Can't divide by 0!"

