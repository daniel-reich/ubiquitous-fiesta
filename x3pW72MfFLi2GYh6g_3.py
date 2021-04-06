
def is_scalable(lst):
  return all(b-5 <= a <= b+5 for a, b in zip(lst, lst[1:]))

