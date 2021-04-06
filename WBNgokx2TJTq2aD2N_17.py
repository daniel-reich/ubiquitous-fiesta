
def smallest(digits, value):
  result = 0
  while len(str(result))<digits:
    result += value
  return result

