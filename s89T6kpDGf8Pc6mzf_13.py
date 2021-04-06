
def seven_segment(txt):
  chk = {'0':set('abcdef'),
  '1':set('bc'),
  '2':set('abdeg'),
  '3':set('abcdg'),
  '4':set('bcfg'),
  '5':set('acdfg'),
  '6':set('acdefg'),
  '7':set('abc'),
  '8':set('abcdefg'),
  '9':set('abcfg')
  }
  curr,res = txt[0],[]
  for i in txt[1:]:
    turn_on = {c.upper() for c in chk[i]-chk[curr]}
    turn_off = chk[curr]-chk[i]
    res.append(sorted(turn_on|turn_off,key=lambda x:x.lower()))
    curr = i
  return res

