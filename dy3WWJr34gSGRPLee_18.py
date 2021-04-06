
def make_box(n):
  lst = []
  t = n
  while n >= 1:
    if 1 < n < t:
      lst.append("#" + " " * (t-2) + "#")
      n -=1
    else:
      lst.append("#" * t)
      n -= 1
  return lst

