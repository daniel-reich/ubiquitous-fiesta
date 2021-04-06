
def moving_partition(l):
  return [[l[:i], l[i:]] for i in range(1,len(l))]

