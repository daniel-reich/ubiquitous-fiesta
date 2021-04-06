
def unique_styles(albums):
  d = dict()
  total = 0
  for i in range(len(albums)):
    l = albums[i].split(',')
    for j in l:
      if d.get(j) == None:
        d.update({j: 0})
        total = total + 1 
      else:
        d.update({j: d.get(j)+1})
  return total

