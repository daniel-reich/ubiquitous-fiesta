
def stem_plot(lst):
  def stem_leaf_creator(num):
    if num <= 9:
      return [0, num]
    else:
      l = list(str(num))
      stem = l[:-1]
      leaf = l[-1]
      return [stem, leaf]
  def sl_dic_creator(s_and_ls):
​
    sldic = {}
​
    for pair in s_and_ls:
      stem = pair[0]
      leaf = pair[1]
    
      sl = ''
      try:
        for item in stem:
          sl += str(item)
      
        stem = sl
      except TypeError:
        stem = str(stem)
      if stem not in sldic.keys():
        sldic[stem] = [leaf]
      else:
        sldic[stem].append(leaf)
    
    for key in sldic:
      v = sorted(sldic[key])
​
      sldic[key] = v
    
    return sldic
  def sldic_formatter(sldic):
​
    keys = []
​
    for key in sldic:
      keys.append(int(key))
​
    s = sorted(keys)
​
    ns = []
​
    for item in s:
      ns.append(str(item))
​
    s = ns
    del ns
    return s      
  def final_result(sf, sldic):
​
    result = []
​
    for item in sf:
​
      key = item
      v = sldic[key]
​
      v = sorted(v)
      
      kv = '{k} | '.format(k = key)
​
      for item in v:
        kv += str(item) + ' '
      
      result.append(kv)
    
    real_result = []
    
    for r in result:
      l = list(r)
      l.pop(-1)
      s = ''
      for item in l:
        s += item
      real_result.append(s)
​
    return real_result
​
  sandls = []
​
  for n in lst:
    slc = stem_leaf_creator(n)
    sandls.append(slc)
​
  sldic = sl_dic_creator(sandls)
  
  sf = sldic_formatter(sldic)
​
  fr = final_result(sf, sldic)
  
  return fr

