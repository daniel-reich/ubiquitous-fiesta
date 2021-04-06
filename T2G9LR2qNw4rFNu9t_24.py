
def chunk(array, size):
  final = []
  for i in range(0,len(array),size):
    final.append(array[i:i+size])
  return final

