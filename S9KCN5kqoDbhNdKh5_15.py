
def count_characters(lst):
  if len(lst) == 0: return 0
  amount = 0
  for i in lst:
    amount += len(i)
  return amount

