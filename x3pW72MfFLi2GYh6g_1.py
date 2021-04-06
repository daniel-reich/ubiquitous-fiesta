
def is_scalable(lst):
  return all(abs(a-b) <= 5 for a, b in zip(lst, lst[1:]))

