
def isbn13(txt):
  d = {str(n):n for n in range(10)}
  d["X"] = 10
  
  if len(txt)==13 and sum(d[n]*(3**idx%8) for idx,n in enumerate(txt))%10 == 0:
    return "Valid"
  if len(txt)==10 and sum(d[n]*(10-idx) for idx,n in enumerate(txt)) % 11 ==0:
    last = -sum(d[n]*(3**idx%8) for idx,n in enumerate("978"+txt[:-1]))%10
    return "978"+txt[:-1]+str(last)
  return "Invalid"

