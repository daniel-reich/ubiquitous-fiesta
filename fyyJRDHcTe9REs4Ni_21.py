
def check(d1, d2, k):
  if (k in d1 and k not in d2) or (k in d2 and k not in d1):
    return "One's empty"
  else:
    if d1.get(k) == d2.get(k):
      return True
    else:
      return "Not the same"

