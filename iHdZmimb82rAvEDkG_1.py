
def bitwise_index(lst):
  def is_even(n):
    string = str(n)
    return string[-1] in '24680'
  
  def highest_even(lst):
    even = []
    
    for n in lst:
      if is_even(n) == True:
        even.append(n)
    try:
      return max(even)
    except:
      return None
  
  he = highest_even(lst)
  
  def find_index(item, lst):
    for n in range(len(lst)): 
      try:
        if lst[n] == item:
          #print(n)
          return n
      except IndexError:
        pass
    return False
  
  if he == None:
    return 'No even integer found!'
  
  fi = find_index(he, lst)
  index_parity = is_even(fi)
  
  if index_parity == True:
    index_parity = 'even'
  else:
    index_parity = 'odd'
    
  return {'@{} index {}'.format(index_parity, fi): he}

