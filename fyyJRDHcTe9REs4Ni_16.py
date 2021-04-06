
def check(d1, d2, k):
  if k in d1 and k in d2:
    return True if d1[k] == d2[k] else "Not the same"
  return "One's empty"

