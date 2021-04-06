
def sort_by_string(lst, txt):
  x = []
  for i in range(len(txt)):
    for j in range(len(lst)):
      if lst[j].startswith(txt[i]):
        x.append(lst[j])
  return x

