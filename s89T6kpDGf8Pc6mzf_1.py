
def seven_segment(txt):
  s = ["abcdef","bc","abdeg","abcdg","bcfg","acdfg","acdefg","abc","abcdefg","abcfg"]
  seg = {str(n):s[n] for n in range(10)}
  
  def trans(n,m):
    off = [e for e in seg[n] if e not in seg[m]]
    on = [e.upper() for e in seg[m] if e not in seg[n]]
    return sorted(on+off,key = lambda e: e.lower())
  
  return [trans(txt[i],txt[i+1]) for i in range(len(txt)-1)]

