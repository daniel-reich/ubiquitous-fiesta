
def fair_swap(l1, l2):
  swaps = set()
  l1_sum = sum(l1)
  l2_sum = sum(l2)
  for num1 in set(l1):
    for num2 in set(l2):
      if l1_sum - num1 + num2 == l2_sum - num2 + num1:
        swaps.add((num1, num2))
  return swaps

