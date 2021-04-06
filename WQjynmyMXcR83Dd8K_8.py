
def number_of_swaps(lst):
  swap = 0
  while True:
    for i in range(len(lst)-1):
      if lst[i] > lst[i+1]:
        lst[i], lst[i+1] = lst[i+1], lst[i]
        swap += 1
    if lst == sorted(lst):
      break
  return swap

