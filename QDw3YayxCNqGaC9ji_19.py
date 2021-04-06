
def make_change(c):
  q=c//25
  d=(c-q*25)//10
  n = (c-q*25-d*10)//5
  p = c-q*25-d*10-n*5
  return {"q": q, "d": d, "n":n, "p": p}

