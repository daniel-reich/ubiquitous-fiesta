
def simple_pair(lst, n):
  for ndx, i in enumerate(lst, start=1):
    if i and not n%i:
      if n//i in lst[ndx:]:
        return [i, n//i]

