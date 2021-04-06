
def shared_digits(lst):
  l = len(lst)
  for i in range(1,len(lst)):
    if len(set(str(lst[i])).intersection(set(str(lst[i-1])))) == 0:
      return False
  return True

