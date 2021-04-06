
def sum_missing_numbers(lst):
  lst = sorted(lst)
  total = 0
  for i in range(len(lst)-1):
    if lst[i+1] - lst[i] != 1:
      for i in range(lst[i]+1,lst[i+1]):
        total += i
  return total

