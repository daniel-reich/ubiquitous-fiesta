
def jazzify(lst):
  l = []
  for i in lst:
    if i[-1] == "7":
      l.append(i)
      continue
    else:
      l.append(i+"7")
  return l

