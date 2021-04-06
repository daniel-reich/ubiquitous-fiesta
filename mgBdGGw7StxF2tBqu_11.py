
def duplicates(txt):
  lst1 = []
  for i in txt.strip():
    if i not in lst1:
      lst1.append(i)
  return len(txt) - len(lst1)

