
def stem_plot(lst):
​
  lst = sorted(lst)
  nums = [str(x) if x>9 else'0'+str(x) for x in lst]
  
  nd = {}
  
  for i in nums:
    if len(nd)>0:
      if i[:-1] not in list(nd.keys()):
        nd[i[:-1]] = i[-1]
      else:
        nd[i[:-1]] += ' ' + i[-1]
    else:
      
      nd[i[:-1]] = i[-1]
      
  keys = list(map(str,sorted( [ int(x) for x in list( nd.keys() ) ] )))
  
  return ['{} | {}'.format(key,nd[key]) for key in keys]

