
def nespers(lst):
  def factorial(num):
    product = 1
    
    for n in range(1, num+1):
      product *= n
    
    return product
  def unpack(lst):
    lists = []
    lengths = []
    
    for item in lst:
      if isinstance(item, list) == True:
        lists.append(item)
        lengths.append(len(item))
    
    newlists = []
    
    for lst in lists:
      for item in lst:    
        if isinstance(item, list) == True:
          newlists.append(item)
          lengths.append(len(item))
    
    lists = newlists
    newlists = []
    
    for lst in lists:
      keep = True
      for item in lst:
        if isinstance(item, list) == True:
          newlists.append(item)
          lengths.append(len(item))
          keep = False
      if keep == True:
        newlists.append(item)
    
    lists = newlists
    newlists = []
    
    return lengths
    
  lengths = [len(lst)]
  unpacked = unpack(lst)
  
  for length in unpacked:
    lengths.append(length)
  print(lengths, unpacked)
  factorials = []
  
  for length in lengths:
    factorials.append(str(factorial(length)))
  
  return eval('*'.join(factorials))

