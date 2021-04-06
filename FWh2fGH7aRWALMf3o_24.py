
def cleave(string, lst):
  result = []
  lst.sort(key = lambda x: len(x), reverse = True)
  for i in lst:
    while i in string:
      result.append([string.find(i), i])
      string = string[:string.find(i)] + "."*len(i) + string [string.find(i)+len(i):]
  result.sort()
  result = [x[1] for x in result]
  if not string == "."*len(string): return 'Cleaving stalled: Word not found'
  return " ".join(result)

