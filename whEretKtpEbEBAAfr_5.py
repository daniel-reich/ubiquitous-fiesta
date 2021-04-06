
def cms_selector(lst, txt):
  return sorted(lst) if len(txt) == 0 else sorted([i for i in lst if txt in i.lower()])

