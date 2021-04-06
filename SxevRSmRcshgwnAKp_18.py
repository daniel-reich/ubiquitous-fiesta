
def pricey_prod(d):
  sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)
  l = []
  for item in sorted_dict:
    if item[1] < 500:
      return l
    else:
      l.append(item[0])
    
  return l

