
def can_alternate(s):
  return -1<=sum(-1 if x=='0' else 1 for x in s)<=1

