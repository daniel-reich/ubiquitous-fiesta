
def factor_chain(lst):
  for i, num in enumerate(lst):
    if i == 0:
      continue
    if num % lst[i-1] != 0:
      return False
  return True

