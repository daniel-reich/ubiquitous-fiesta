
def fauna_number(txt):
  animals = sorted(["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"])
  txt = txt.replace(',',' ').split()
  ret = []
  for i in animals:
    if i in txt:
      ret.append((i,txt[txt.index(i)-1]))
  return ret

