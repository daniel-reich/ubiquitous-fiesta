
def grouping(w):
  keys = sorted(set([sum([j.isupper() for j in i]) for i in w]))
  dic = {k:[] for k in keys}
  for i in sorted(w, key=lambda x: x.lower()):  
    dic[sum([j.isupper() for j in i])].append(i)
  return dic

