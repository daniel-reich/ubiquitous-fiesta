
def make_grlex(lst):
  res = []
  mn = min(len(i) for i in lst)
  mx = max(len(i) for i in lst)
  for i in range(mn,mx+1):
    temp = []
    for word in lst:
      if len(word) == i: temp.append(word)
    res += sorted(temp)
  return res

