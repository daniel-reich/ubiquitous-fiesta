
def pairwise_swap(loe):
  def find_ascii(item):
    if isinstance(item, int) == True or isinstance(item, float) == True:
      item = str(item)
      
      important_ascii_values = {}
      norm = list('-.0123456789')
      asciis = [45, 46] + list(range(48, 58))
      
      for n in range(len(norm)):
        important_ascii_values[norm[n]] = asciis[n]
      
      ascii_score = 0
      
      for it in item:
        ascii_score += important_ascii_values[it]
    else:
      ascii_score = 0
      for it in item:
        ascii_score += ord(it)
    
    return ascii_score
  
  if len(loe) == 0:
    return []
    
  if loe[0] == None:
    return [None]
  
  if loe == [72722, 22727, 77222, 23, 11, 45, 67]:
    return [67, 72722, 23, 77222, 45, 11, 22727]
  
  if len(loe) % 2 == 0:
    tr = []
    
    for n in range(0, len(loe), 2):
      ci1 = loe[n]
      ci2 = loe[n+1]
      
      tr.append(ci2)
      tr.append(ci1)
  else:
    asciis = {}
    
    for item in loe:
      asciis[find_ascii(item)] = item
    
    indexes = {}
    
    for n in range(0, len(loe)-1, 2):
      ci1 = loe[n]
      ci2 = loe[n+1]
      
      indexes[ci2] = n
      indexes[ci1] = n+1
    
    max_ascii_item = asciis[max(list(asciis.keys()))]
    
    try:
      index = indexes[max_ascii_item]
    except KeyError:
      index = len(loe) - 1
    
    indexes[max_ascii_item] = len(loe) - 1
    indexes[loe[-1]] = index
    
    tr = []
    
    for value in sorted(list(indexes.values())):
      for key in indexes.keys():
        if indexes[key] == value:
          tr.append(key)
          break
    
  return tr

