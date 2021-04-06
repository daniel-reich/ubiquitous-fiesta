
def find_bob(names):
  count = -1
  for i in range(0, len(names)):
    if names[i] == 'Bob':
      return i
  
  return count

