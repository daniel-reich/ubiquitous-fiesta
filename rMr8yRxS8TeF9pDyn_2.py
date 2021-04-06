
def war_of_numbers(l):
  o=e=0
  for x in l:
    if x%2:o+=x
    else:e+=x
  return abs(o-e)

