
def diamond_arrays(x):
  def create_half(size):
    if size == 1:
      return [1]
    elif size < 1:
      return []
    else:
      return [size] * size + create_half(size - 1)
  def nest(lst):
    nests = []
    prev = 0
    nest = []
    
    for n in range(len(lst)):
      item = lst[n]
      if item != prev:
        if nest != []:
          nests.append(nest)
        nest = [item]
        prev = item
      else:
        nest.append(item)
    
    if nest != []:
      nests.append(nest)
    
    return nests
        
  
  front_half = list(reversed(create_half(x-1)))
  back_half = create_half(x)
  
  return nest(front_half + back_half)

