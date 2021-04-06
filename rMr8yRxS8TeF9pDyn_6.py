
def war_of_numbers(lst):
  odd=0
  even=0
  for i in lst:
    if i%2 == 0:
      even+=i
    else:
      odd+=i
  if odd > even:
    return odd - even
  else:
    return even - odd

