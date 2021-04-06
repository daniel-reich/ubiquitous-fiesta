
def complete_bracelet(l):
  for i in range(len(l)//2, 1, -1):
    p = l[:i]
    if p * (len(l)//len(p)) == l:
      return True
  return False

