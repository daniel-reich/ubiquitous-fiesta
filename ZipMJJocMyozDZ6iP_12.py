
def group(lst, size):
  lstsize = int(len(lst) / size) + int(len(lst) % size != 0)
  r = [[] for i in range(lstsize)]
  isize = 0
  for i in lst:
    r[isize].append(i)
    isize = (isize + 1) % lstsize
  return r

