
def find_bob(names):
  index = 0
  for x in names:
    if names[index] == 'Bob':
      return index
    else:
      index=index+1
  else:
    return -1

