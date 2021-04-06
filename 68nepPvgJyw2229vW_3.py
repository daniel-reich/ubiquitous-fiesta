
def pairwise_swap(elements):
  index = 0
  new_list = []
  
  while len(elements) > 1:
  
    new_list.append(elements.pop(1))
    new_list.append(elements.pop(0))
  
  if not elements: return new_list
  new_list = new_list + elements
  asciic = [sum([ord(c) for c in str(element)]) for element in new_list]
  asciic_max = max(asciic)
  track = sum([value == asciic_max for value in asciic])
​
  if track == 1:
    index = asciic.index(asciic_max)
    new_list[-1], new_list[index] = new_list[index], new_list[-1]
  
  if track > 1:
    new_list[-1], new_list[0] = new_list[0], new_list[-1]
​
  return new_list

