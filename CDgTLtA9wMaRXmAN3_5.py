
def space_me_out(s):
  i = 0
  t = ""
  for x in s:
    if i == len(s)-1:
      t = t + x
    else:
      t = t + x + " "
    i = i + 1
  return t

