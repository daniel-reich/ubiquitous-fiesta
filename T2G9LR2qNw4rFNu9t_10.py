
def chunk(array, n):
  return [array[i:n+i] for i in range(0,len(array)+1//n+1,n) if array[i:n+i] != []]

