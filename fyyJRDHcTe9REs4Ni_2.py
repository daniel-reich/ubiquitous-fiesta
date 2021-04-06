
def check(d1, d2, k):
  try: return ["Not the same", True][d1[k] == d2[k]]
  except KeyError: return "One's empty"

