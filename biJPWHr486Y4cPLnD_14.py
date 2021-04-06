
def chunkify(lst, size):
  return [lst[i * size:(i + 1) * size] for i in range((len(lst) + size - 1) // size)]

