
def merge_arrays(a, b):
  
  result = []
  k = len(a)
  m = len(b)
  
  for x in range(max(k, m)):
    try:
      result.append(a[x])
    except:
      pass
    try:
      result.append(b[x])
    except:
      pass
  
  return result

