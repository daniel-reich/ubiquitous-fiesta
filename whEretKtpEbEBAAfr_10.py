
def cms_selector(lst, txt):
  lst = [x for x in lst if txt in x]
  lst.sort()
  return lst

