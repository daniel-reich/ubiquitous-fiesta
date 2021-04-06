
def check(d1, d2, k):
  if k in d1 and k in d2:
    if d1.get(k) == d2.get(k):
      return True
    return 'Not the same'
  return "One's empty"

