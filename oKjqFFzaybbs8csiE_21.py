
def cons(lst):
  if len(set(lst)) != len(lst):
    return False
  else:
    lst.sort()
    i = 0
    for num in lst:
      if i == 0:
        i += 1
        continue
      else:
        if num - lst[i - 1] != 1:
          return False
        i += 1
  return True

