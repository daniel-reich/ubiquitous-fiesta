
def number_of_swaps(lst):
  count = 0
  while lst != sorted(lst):
    for i in range(len(lst) - 1):
      if lst[i] <= lst[i+1]:
        continue
      else:
        lst[i], lst[i+1] = lst[i+1], lst[i]
        count += 1
  return count

