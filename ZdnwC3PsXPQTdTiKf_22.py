
def calculator(num1, operator, num2):
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/" and num2 != 0:
    return num1 / num2
  else:
    return "Can't divide by 0!"

