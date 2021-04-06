
def unravel(txt):
  if '[' not in txt: return [txt]
  ret = []
  start = txt.index('[')
  end = txt.index(']')
  switches = txt[start+1:end].split('|')
  
  for switch in switches:
    toadd = txt[:start] + switch + txt[end+1:]
    if '[' in toadd:
      for option in unravel(toadd):
        ret.append(option)
    else:
      ret.append(toadd)
  return sorted(ret)

