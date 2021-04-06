
def jazzify(lst):
  a = []
  for i in range(len(lst)):
    if lst[i].endswith("7"):
      a.append(lst[i])
    else:
      a.append(lst[i] + '7')
  return a

