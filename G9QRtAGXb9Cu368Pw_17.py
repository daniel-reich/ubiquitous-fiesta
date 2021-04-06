
def combinations(*items):
  if type(items) == int:
    return items
  answer = 1
  for i in items:
    if i != 0:
      answer *= i
  return answer

