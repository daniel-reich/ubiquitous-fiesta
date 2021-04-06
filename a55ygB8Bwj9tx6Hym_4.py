
def steps_to_convert(txt):
  lst = [1 if i.isupper() else 0 for i in txt]
  return lst.count(1) if lst.count(1) < lst.count(0) else lst.count(0)

