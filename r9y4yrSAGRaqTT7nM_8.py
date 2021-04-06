
def find_missing(lst):
  if not lst: return False
  lst = sorted(len(i) for i in lst)
  if min(lst)==0: return False
  for i in range(min(lst),max(lst)+1):
    if i not in lst:
      return i

