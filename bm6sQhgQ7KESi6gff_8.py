
def find_the_difference(s, t):
  for a in s:
    if a in t:
      t = t.replace(a,'',1)
  return t

