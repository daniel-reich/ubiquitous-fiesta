
def seven_segment(txt):
  D={'0':('abcdef','g'),
  '1':('bc','adefg'),
  '2':('abdeg','cf'),
  '3':('abcdg','ef'),
  '4':('bcfg','ade'),
  '5':('acdfg','be'),
  '6':('acdefg','b'),
  '7':('abc', 'defg'),
  '8':('abcdefg',''),
  '9':('abcfg','de')}
  res=[[] for _ in range(len(txt)-1)]
  for i in range(len(txt)-1):
    for x in D[txt[i]][0]:
      if x in D[txt[i+1]][-1]:
        res[i].append(x)
    for y in D[txt[i]][-1]:
      if y in D[txt[i+1]][0]:
        res[i].append(y.upper())
  B=[sorted(x, key=lambda t: t.lower()) for x in res]
  return B

