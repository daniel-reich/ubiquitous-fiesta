
def seven_segment(txt,c=None):
  seg = {0:'abcdef', 1:'bc', 2:'abdeg', 3:'abcdg', 4:'bcfg', 5:'acdfg',
       6:'acdefg', 7:'abc', 8:'abcdefg', 9:'abcfg'}
  res = []
  for n in map(int,txt):
    if c != None:
      temp = []
      for ch in 'abcdefg':
        if ch not in seg[n] and ch in seg[c]:
          temp.append(ch)
        elif ch in seg[n] and ch not in seg[c]:
          temp.append(ch.upper())
      res.append(temp)
    c = n
  return res

