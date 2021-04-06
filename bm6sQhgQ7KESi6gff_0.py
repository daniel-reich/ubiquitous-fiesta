
def find_the_difference(s, t):
  for i in s:
    t = t.replace(i,'',1)
  return t

