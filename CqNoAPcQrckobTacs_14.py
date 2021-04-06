
def missing_letter(lst):
  index = ord(lst[0])
  counter = 1
  for i in range(index + 1, index + len(lst)):
    if ord(lst[counter]) != i: 
      return chr(i)
    counter += 1
  return None

