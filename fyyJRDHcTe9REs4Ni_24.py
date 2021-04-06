
def check(d1, d2, k):
  if k in d1 and k in d2:
    if d1[k]==d2[k]:
      return True
    else:
      return "Not the same"
  elif (k in d1 and k not in d2) or (k not in d1 and k in d2):
    return "One's empty"

