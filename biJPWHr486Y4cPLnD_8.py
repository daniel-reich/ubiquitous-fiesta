
def chunkify(lst, size):
  if len(lst) <= size: return [lst]
  return [lst[i:i+size] for i in range(0, len(lst), size)]

