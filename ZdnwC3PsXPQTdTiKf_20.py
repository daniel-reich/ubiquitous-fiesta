
def calculator(num1, operator, num2):
  if operator == "/" and num2 == 0 :
    return "Can't divide by 0!"
  return eval(str(num1) + operator + str(num2))

