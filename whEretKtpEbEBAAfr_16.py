
def cms_selector(lst, txt):
  if txt == "":
    return sorted(lst)
  else:
    return sorted([i for i in lst if txt in i])

