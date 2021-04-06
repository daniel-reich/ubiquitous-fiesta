
def cms_selector(lst, txt):
  lst = [i for i in lst if txt in i.lower()]
  lst.sort()
  return lst if txt else lst

