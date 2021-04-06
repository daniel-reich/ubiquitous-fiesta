
def check_pattern(lst, pattern):
  patt = list(pattern)
  return [patt.index(x) for x in patt] == [lst.index(x) for x in lst]

