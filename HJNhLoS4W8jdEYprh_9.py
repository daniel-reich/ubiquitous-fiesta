
def list_between(num1, num2, lst):
  result = []
  for num in lst:
    if num2 > num > num1:
      result.append(num)
  return result

