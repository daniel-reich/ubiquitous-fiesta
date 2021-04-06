
def number_of_swaps(lst):
​
  count = 0
​
  while True:
    if all(lst[i] <= lst[i + 1] for i in range(len(lst)-1)):
      return(count)
      break
​
    for i in range(len(lst)-1):
      if lst[i] > lst[i+1]:
        lst[i], lst[i+1] = lst[i+1], lst[i]
        count += 1

