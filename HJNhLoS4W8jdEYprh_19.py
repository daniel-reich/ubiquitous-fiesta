
def list_between(num1, num2, lst):
  result = []
  for item in lst:
    if item > num1 and item < num2:
      result.append(item)
  return result

