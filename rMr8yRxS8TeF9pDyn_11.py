
def war_of_numbers(lst):
  odd = 0
  even = 0
  for i in lst:
    if i % 2:
      odd += i
    else:
      even += i
  return abs(odd - even)

