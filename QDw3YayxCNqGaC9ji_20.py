
def make_change(c):
  q = (c - c % 25)
  d = (c - q) - (c - q) % 10
  p = ((c - q) % 10) % 5
  n = ((c - q) % 10) - p
  return {"q": q//25, "d": d//10, "n": n//5, "p": p}

