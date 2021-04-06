
def cms_selector(lst, txt):
  a =[]
  for i in lst:
    if txt in i:
      a.append(i)
  return sorted(a)

