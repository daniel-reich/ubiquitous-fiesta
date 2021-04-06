
def sort_by_last(txt):
  lst, a = txt.split(' '), []
  char = sorted([i[-1] for i in lst])
  for i in char:
    for j in lst:
      if i == j[-1] and j not in a:
        a.append(j)
  return ' '.join(a)

