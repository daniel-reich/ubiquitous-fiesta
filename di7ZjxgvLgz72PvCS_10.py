
def validate_swaps(lst, txt):
  return [len(x) == len(txt) and sum(a != b for a, b in zip(x, txt)) == 2 for x in lst]

