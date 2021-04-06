
def is_polydivisible(n):
  cur = 1
  while cur<=len(str(n)):
    if not (int(str(n)[:cur])/cur).is_integer():
      return False
    cur+=1
  return True

