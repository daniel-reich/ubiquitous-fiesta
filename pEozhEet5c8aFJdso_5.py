
def all_about_strings(txt):
  lst = []
  mid = len(txt) // 2
  lst.append(len(txt))
  lst.append(txt[0])
  lst.append(txt[-1])
  if len(txt) % 2 == 0:
    lst.append(txt[mid - 1:mid + 1])
  else:
    lst.append(txt[mid])
  for i in txt:
    if txt.count(i) >= 2:
      lst.append('@ index ' + str(txt.index(i, txt.index(i) + 1)))
      break
  if len(lst) != 5:
      lst.append('not found')
  return lst

