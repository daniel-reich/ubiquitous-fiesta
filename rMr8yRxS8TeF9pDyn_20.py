
def war_of_numbers(lst):
  even = 0
  odd = 0
  for num in lst:
    if num % 2 == 0: # even
      even += num
    else:
      odd += num
  
  if even > odd:
    return even - odd
  elif odd > even:
    return odd - even
  else:
    return 0

