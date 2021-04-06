
def largest_gap(lst):
  s=sorted(lst)
  return max(y-x for x,y in zip(s[:-1],s[1:]))

