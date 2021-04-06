
def max_separator(txt):
  res = {}
  for i,c in enumerate(txt):
    for j in range(i+1,len(txt)):
      if txt[j] == c:
        if c not in res or res[c] < j+1-i:
          res[c] = j+1-i
        break
  return sorted([k for k,v in res.items() if v == max(res.values())]) if res else []

