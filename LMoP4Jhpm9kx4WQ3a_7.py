
def is_ascending(s):
  for n in range(len(s)-1,0,-1):
    if not len(s)%n:
      lst = [int(s[i:i+n]) for i in range(0, len(s), n)]
      if all(lst[i] + 1 == lst[i+1] for i in range(len(lst)-1)):
        return True
  return False

