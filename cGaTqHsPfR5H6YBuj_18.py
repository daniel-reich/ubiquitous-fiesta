
def make_sandwich(i, f):
  new_list = []
  for n in i:
    if n == f:
      new_list.append("bread")
      new_list.append(n)
      new_list.append("bread")
    else:
      new_list.append(n)
  return new_list

