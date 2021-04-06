
def complete_bracelet(lst):
  for n in range(2, len(lst)//2 + 1):
    groups = [lst[i:i+n] for i in range(0, len(lst), n)]
    if groups.count(groups[0]) == len(groups):
      return True
  return False

