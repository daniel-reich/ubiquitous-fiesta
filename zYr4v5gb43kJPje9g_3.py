
def moving_partition(lst):
  partitions = []
  for i in range(len(lst)-1):
    partitions.append([lst[0:i+1],lst[i+1:]])
  return partitions

