
def complete_bracelet(lst):
  llst = len(lst)
  factors = set()
  for j in range(2,int(llst**0.5)+1):
    if llst%j == 0:
      factors.add(j)
      factors.add(llst//j)
  factors = sorted(list(factors))
​
  for f in factors:
    if lst[:f] * (llst//f) == lst: return True
  return False

