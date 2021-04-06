
def war_of_numbers(lst):
  even = 0
  odd = 0
  for i in range(len(lst)):
    if not lst[i] % 2:
      even += lst[i]
    else:
      odd += lst[i]
  return abs(even - odd)

