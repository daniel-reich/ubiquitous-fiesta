
def zero_indices(lst, k):
  max_length = 0
  index = 0
  flips = k
  for i in range(len(lst)):
    length = 0
    for j in range(i, len(lst)):
      if lst[j] == 0:
        if flips == 0: break
        flips -= 1
      length += 1
    if length > max_length:
      max_length = length
      index = i
    flips = k
  indicies = []
  for i in range(index, min(len(lst), index + max_length)):
    if lst[i] == 0:
      indicies.append(i)
  return indicies

