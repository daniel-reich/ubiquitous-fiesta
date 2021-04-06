
def inator_inator(inv):
  lst = list(inv)
  if lst[len(lst)-1] in 'aeiouAEIOU':
    lst.append("-inator {}000".format(len(lst)))
  else:
    lst.append("inator {}000".format(len(lst)))
  return "".join(lst)

