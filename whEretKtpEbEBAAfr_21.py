
def cms_selector(lst, txt):
  return sorted([i for i in lst if txt in i], key=lambda x:ord(x[0]))

