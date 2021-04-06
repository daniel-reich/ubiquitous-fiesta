
def jazzify(lst):
  for i in range(len(lst)):
    if "7" in lst[i]:
      continue
    else:
      lst[i] = lst[i]+"7"
  return lst

