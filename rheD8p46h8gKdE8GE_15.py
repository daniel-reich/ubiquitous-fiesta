
def grayscale(lst):
  for a in range(len(lst)):
    for b in range(len(lst[a])):
      md = round(sum([255 if _ > 255 else 0 if _ < 0 else _ for _ in lst[a][b]])/len(lst[a][b]))
      for c in range(len(lst[a][b])):
        lst[a][b][c] = md
  return lst

