
def pyramidal_string(string, _type):
  f = [x for x in range(1,len(string))]
  fact = [sum(f[:x]) for x in range(1,len(string))]
  i = 0
  s = list(string)
  L = []
  l = []
  if not string:  return []
  elif len(string)==1:  return [string]
  elif len(string) not in fact: return 'Error!'
  elif _type == 'REG':
    for x in range(2,fact.index(len(s))+2):
      l = s[i+1:i+x+1]
      L.append(l)
      l = []
      i = i+x
    return [s[0]] + [' '.join(x) for x in L]
  else:
    for x in range(fact.index(len(s))+1, 1,-1):
      l = s[i:i+x]
      L.append(l)
      l = []
      i = i+x
    return [' '.join(x) for x in L] + [s[-1]]

