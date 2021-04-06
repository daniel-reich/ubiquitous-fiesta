
def group(lst, size):
  l = len(lst)
  n = l//size + 1 - 0**(l%size)
  return [[x for x in range(i,l+1,n)] for i in range(1,n+1)]

