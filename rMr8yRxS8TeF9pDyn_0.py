
def war_of_numbers(lst):
  return abs(sum(n if n%2 else -n for n in lst))

