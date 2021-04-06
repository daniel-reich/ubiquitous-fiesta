
def combine(lst):
  keys = set([lst[i][0] for i in range(len(lst))])
  result = {}
  for key in sorted(keys):
    result[key] = []
  
  for i in range(len(lst)):
    result[lst[i][0]].append(lst[i][2]) 
    
  return result

