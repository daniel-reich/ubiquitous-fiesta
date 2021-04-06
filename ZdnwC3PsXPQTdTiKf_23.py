
def calculator(num1, operator, num2):
  if operator == "/" and num2 == 0:
    return "Can't divide by 0!"
  string = str(num1) + operator + str(num2) 
  return eval(string)

