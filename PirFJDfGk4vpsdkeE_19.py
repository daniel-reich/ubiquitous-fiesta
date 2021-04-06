
def help_bobby(size):  
  array = [i[:] for i in [[0]*size]*size]
  for x in range(size): array[x][x] = array[x][size-x-1] = 1
  return array

