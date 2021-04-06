
def filter_factorials(numbers):
  facts = []
  for a in numbers:
    prod = 1
    for b in range(1,a+1):
      prod = prod*b
      if prod == a:
        facts.append(a)
        break
  return facts

