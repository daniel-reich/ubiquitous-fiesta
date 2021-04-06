
def calculator(num1, operator, num2):
  try:
    return eval("{}{}{}".format(num1, operator, num2))
  except ZeroDivisionError:
    return "Can't divide by 0!"

