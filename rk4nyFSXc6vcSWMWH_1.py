
def shared_digits(lst):
  combined = [[a, b] for a, b in zip(lst, lst[1:])]
  one = set(x for y in [x for x in combined if any(i in str(x[0]) for i in str(x[1]))] for x in y)
  return [x for x in lst if x in one] == lst

