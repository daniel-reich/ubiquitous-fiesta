
s = {'0': 'abcdef', '1': 'bc', '2': 'abdeg', '3': 'abcdg', '4': 'bcfg',
      '5': 'acdfg', '6': 'acdefg', '7': 'abc', '8': 'abcdefg', '9': 'abcfg'}
​
def seven_segment(txt):
  if len(txt) < 2: return []
  r = []
  for x, y in zip(txt, txt[1:]):
    if x == y:
      r.append([])
    else:
      c = []
      for i in set(s[y]) - set(s[x]):
        c.append(i.upper())
      for i in set(s[x]) - set(s[y]):
        c.append(i)
      c.sort(key=str.lower)
      r.append(c)
  return r

