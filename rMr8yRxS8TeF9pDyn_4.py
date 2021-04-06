
def war_of_numbers(lst):
  return abs(sum(lst) - 2*sum(x for x in lst if x%2))

