
def check(d1, d2, k):
  try:
    if d1[k] != d2[k]:
      return 'Not the same'
    return True
  except KeyError:
    return "One's empty"

