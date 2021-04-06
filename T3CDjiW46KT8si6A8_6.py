
def product(lst):
  maks = second = max(lst)
  for x in sorted(lst,reverse=True):
    if x < second:
      second = x
      break
  return maks * second

