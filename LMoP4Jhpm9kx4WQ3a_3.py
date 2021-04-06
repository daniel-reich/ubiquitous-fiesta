
def is_ascending(s):
  lst = list(s)
  for n in range(1, len(lst)//2+1):
    groups = [int("".join(lst[i:i + n])) for i in range(0, len(lst), n)]
    if list(sorted(set(groups))) == groups and (groups[0] + groups[-1]) / 2 == sum(groups) / len(groups) and groups[0] == groups[1]-1:
      return True
      
  return False

