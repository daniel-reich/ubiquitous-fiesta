
def operation(num1, num2):
  if num1*num2==24:
    return "multiplied"
  if num1/num2==24 or num2/num1==24:
    return "divided"
  if num1+num2==24:
    return "added"
  if num1-num2==24 or num2-num1==24:
    return "subtracted"
  else:
    return None

