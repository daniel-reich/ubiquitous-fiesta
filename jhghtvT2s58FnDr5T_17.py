
def jazzify(lst):
  out = []
  for i in lst:
    if i[-1] != "7":
      out.append(i + "7")
    else:
      out.append(i)
  return out

