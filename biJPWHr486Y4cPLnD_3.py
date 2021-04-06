
def chunkify(lst, size):
  chonks = []
  for i in range(len(lst)):
    if i%size == 0:
      chonks.append(lst[i:i+size])
  return chonks

