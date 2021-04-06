
def less_or_equal(lst, k):
  if not k:
    if min(lst) in [0,1]:
      return None
    else:
      return 1
  s=sorted(lst)
  i=s[k-1]
  if k!=len(s) and i==s[k]:
    return None
  return i

