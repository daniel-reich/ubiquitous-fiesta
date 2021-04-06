
def get_frequencies(lst):
  dct=dict.fromkeys(lst)
  for x,y in dct.items():
    dct[x]=lst.count(x) 
  return dct

