
def chunk(array, size):
  
  chunks = []
  l = []
  c = 0
  
  while c < len(array):
    if len(l) == size:
      chunks.append(l)
      l = []
    l.append(array[c])
    c += 1
  
  if len(l) > 0:
    chunks.append(l)
  
  del l
  
  return chunks

