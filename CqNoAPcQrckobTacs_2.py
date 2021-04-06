
def missing_letter(lst):
  start = ord(lst[0])
  for i in lst: 
    if (ord(i) != start): 
      return chr(start)
    start += 1

