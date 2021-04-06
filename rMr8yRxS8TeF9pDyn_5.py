
def war_of_numbers(lst):
  even = 0
  odd = 0
  for i in lst:
    if i % 2 == 0:
      even += i
    else:
      odd += i
  if even > odd:
    return even - odd
  else:
    return odd - even

