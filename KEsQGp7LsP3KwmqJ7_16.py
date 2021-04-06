
def check(lst):
  sortedLst = sorted(lst)
  for i in range(1, len(lst)):
    if lst == sortedLst[i:] + sortedLst[:i]:
      return "YES"
  return "NO"

