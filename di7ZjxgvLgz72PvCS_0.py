
def validate_swaps(lst, txt):
  return [sum(a != b for a, b in zip(s, txt)) == 2 and len(s) == len(txt) for s in lst]

