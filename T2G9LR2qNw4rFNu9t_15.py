
def chunk(array, size):
  return [array[i * size:(i * size) + size] for i in range(round(len(array) / size) + 1)
      if array[i * size:(i * size) + size] != []]

