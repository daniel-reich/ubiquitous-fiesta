
def trouble(num1, num2):
  num1 = str(num1)
  num2 = str(num2)
  triples = [c * 3 for c in "0123456789"]
  doubles = [c * 2 for c in "0123456789"]
  for t, d in zip(triples, doubles):
    if t in num1 and d in num2:
      return True
  return False

