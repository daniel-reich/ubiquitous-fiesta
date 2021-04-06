
def war_of_numbers(lst):
  odd = 0
  even = 0
  for x in lst:
    if x in list(range(1, 1000, 2)):
      odd += x
    else:
      even += x
  if odd > even:
    return odd - even
  else:
    return even - odd

