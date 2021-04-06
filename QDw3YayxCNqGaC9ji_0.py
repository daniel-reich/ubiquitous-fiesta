
def make_change(c):
  return {"q": c//25, "d": c%25//10, "n": c%25%10//5, "p": c%5}

