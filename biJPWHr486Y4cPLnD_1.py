
def chunkify(lst, size):
  a = []
  for i in range(0, len(lst), size):
    a.append(lst[i:i+size])
  return a

