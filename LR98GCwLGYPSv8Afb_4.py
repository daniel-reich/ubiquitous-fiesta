
def pluralize(lst):
  base = set(lst)
  return {item + 's'*(lst.count(item)>1) for item in base}

