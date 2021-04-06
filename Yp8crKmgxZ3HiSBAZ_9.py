
def freq_count(lst, el):
  def find_nesting(lst, n=0):
    items = []
    lists = []
​
    for item in lst:
      if isinstance(item, list) == True:
        for i in item:
          lists.append(i)
      else:
        items.append([n, item])
    
    if len(items) == 0:
      items.append([n, 'N'])
    if len(lists) == 0:
      return items
    else:
      return items + find_nesting(lists, n+1)
  
  nesting = find_nesting(lst)
  nests = {}
​
  for nest in nesting:
    nst = nest[0]
    item = nest[1]
​
    if nst not in nests.keys():
      nests[nst] = [item]
    else:
      nests[nst].append(item)
  
  frequency = []
  
  for freq in nests.keys():
    lst = nests[freq]
    count = lst.count(el)
    
    frequency.append([freq,count])
  
  return frequency

