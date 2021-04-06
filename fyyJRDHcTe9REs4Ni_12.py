
def check(d1, d2, k):
  if not d1.get(k) or not d2.get(k):
    return "One's empty"
  return True if d1.get(k) == d2.get(k) else "Not the same"

