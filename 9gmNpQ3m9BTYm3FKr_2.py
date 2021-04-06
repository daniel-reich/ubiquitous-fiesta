
def lucky_seven(lst):
  for x in lst:
    a=lst.copy()
    a.remove(x)
    for y in a:
      b=a.copy()
      b.remove(y)
      for z in b:
        if x+y+z==7:
          return True
  return False

