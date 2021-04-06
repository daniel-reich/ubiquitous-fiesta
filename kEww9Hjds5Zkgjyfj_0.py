
def replace_next_largest(lst):
  s = sorted(lst) + [-1]
  return [s[s.index(i)+1] for i in lst]

