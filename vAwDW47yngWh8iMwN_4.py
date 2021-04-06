
def cap_last(txt):
  txt = txt.split(" ")
  lst = []
  for i in txt:
    i = i[0:-1]+i[-1].upper()
    lst.append(i)
  return ' '.join(lst)

