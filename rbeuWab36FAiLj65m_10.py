
def grouping(w):
  def cap_count(words):
    
    cc = {}
​
    for word in words: 
      c = 0
​
      for l8r in word:
        t = l8r.isupper()
​
        if t == True:
          c += 1
      
      key = c
      v = word
​
      if key not in cc.keys():
        cc[key] = [v]
      else:
        cc[key].append(v)
  
    ncc = {}
​
    for key in sorted(cc.keys()):
      v = cc[key]
      v.sort()
      ncc[key] = v
    
    return ncc
  def lexicon_order(value):
    
    conversions = {}
    nv = []
​
    for v in value:
      nv.append(v.lower())
      conversions[v.lower()] = v
    
    nv.sort()
​
    tr = []
​
    for item in nv:
      tr.append(conversions[item])
    
    return tr
​
  cc = cap_count(w)
  tr = {}
​
  for key in cc.keys():
    
    v = cc[key]
​
    nv = lexicon_order(v)
​
    tr[key] = nv
  
  return tr

