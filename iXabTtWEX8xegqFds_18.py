
def alternate_sort(lst):
  def sort_nums_l8rs(lst):
    numbers = []
    letters = []
    
    for item in lst:
      try:
        numbers.append(int(item))
      except ValueError:
        letters.append(item)
    
    return [sorted(numbers), sorted(letters)]
  def combine(l1, l2):
    combined = []
    
    if len(l1) > len(l2):
      for n in range(len(l2)):
        combined.append(l1[n])
        combined.append(l2[n])
      for n in range(len(l2), len(l1)):
        combined.append(l1[n])
    elif len(l1) < len(l2):
      for n in range(len(l1)):
        combined.append(l1[n])
        combined.append(l2[n])
      for n in range(len(l1), len(l2)):
        combined.append(l2[n])
    else:
      for n in range(len(l1)):
        combined.append(l1[n])
        combined.append(l2[n])
    
    return combined
  
  nums, l8rs = sort_nums_l8rs(lst)
  
  return combine(nums, l8rs)

