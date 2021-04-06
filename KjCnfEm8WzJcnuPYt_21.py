
def zero_indices(lst, k):
  indices = []
  for i,element in enumerate(lst):
    if element == 0:
      indices.append(i)
  
  max_count = 0
  count = 0
  total_zeros = len(indices)
  
  result = []
  
  for i in range(total_zeros - (k - 1)):
    subarr = indices[i: i + k]
    for j in range(len(lst)):
      if lst[j] == 1 or j in subarr:
        count += 1
      else:
        if count > max_count:
          max_count = count 
          result = subarr 
        count = 0
  
  if count > max_count:
    max_count = count
    result = subarr
    
  return result

