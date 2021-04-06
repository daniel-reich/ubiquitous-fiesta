
def check(d1, d2, key):
  try:
    res1, res2 = d1[key], d2[key]
    return True if res1 == res2 else 'Not the same'
  except KeyError:
    return("One's empty")

