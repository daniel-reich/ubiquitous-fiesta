
def cms_selector(lst, txt):
  return sorted(lst) if not txt else sorted([e for e in lst if txt in e.lower()])

