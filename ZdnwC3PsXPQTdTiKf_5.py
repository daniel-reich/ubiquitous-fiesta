
def calculator(num1, operator, num2):
  return "Can't divide by 0!" if operator == '/' and num2 == 0 else eval(str(num1)+operator+str(num2))

