
def chunkify(lst, size):
  out = []
  for i in range(0, len(lst), size):
    out.append(lst[i:i+size])
  return out

