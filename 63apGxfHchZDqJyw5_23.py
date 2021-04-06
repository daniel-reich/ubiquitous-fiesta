
def operation(num1, num2):
  if num1+num2==24:
    return "added"
  elif max(num1,num2)-min(num1,num2)==24:
    return "subtracted"
  elif num1*num2==24:
    return "multiplied"
  elif num1/num2==24:
    return "divided"
  else:
    return None

