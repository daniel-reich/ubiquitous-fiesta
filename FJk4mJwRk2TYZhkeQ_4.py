
def accum(txt):
  lst = []
  for i in range(len(txt)):
    lst.append(txt[i].capitalize() + txt[i].lower() * i)
  new_txt = "-".join(lst)
  return new_txt

