
def calculate_arrowhead(lst):
  links = 0
  rechts = 0
  for pijlen in lst:
    for pijl in pijlen:
      if pijl == ">":
        rechts += 1
      else:
        links += 1
  if links > rechts:
    result = links - rechts
    return "<" * result
  elif links < rechts:
    result = rechts - links
    return ">" * result
  else:
    return ""

