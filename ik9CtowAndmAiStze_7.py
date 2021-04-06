
def frequency_sort(s):
  def freq(string):
    char_freq = {}
    for l8r in set(string):
      freq = string.count(l8r)
      if freq not in char_freq.keys():
        char_freq[freq] = [l8r]
      else:
        char_freq[freq].append(l8r)
    return char_freq
  def cap_sort(dic):
    updated = {}
    for k in dic.keys():
      v = dic[k]
      uv = [l8r for l8r in v if l8r.isupper() == True]
      lv = [l8r for l8r in v if l8r.islower() == True]
      updated[k] = [uv, lv]
    return updated
  def reg_sort(dic):
    updated = {}
    for k in dic.keys():
      v = dic[k]
      nv = ''
      for l8r in sorted(v[0]):
        nv += l8r
      for l8r in sorted(v[1]):
        nv += l8r
      updated[k] = nv
    return updated
  def combine(dic):
    ns = ''
    for k in reversed(sorted(dic.keys())):
      v = dic[k]
      for l8r in v:
        ns += (l8r * k)
    return ns
​
  f = freq(s)
  cs = cap_sort(f)
  rs = reg_sort(cs)
  c = combine(rs)
  
  return c

