
def single_occurrence(txt):
  txt = txt.upper()
  if len(txt) == 0:
    return ""
  count = []
  for a in txt:
    count.append(txt.count(a))
  index = count.index(min(count))
  return txt[index].upper()

